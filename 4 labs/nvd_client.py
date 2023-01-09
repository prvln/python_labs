import aiohttp
import csv
import argparse
import logging
import json
import asyncio

from math import ceil
from dataclasses import dataclass, field
from typing import List



logging.basicConfig(level=logging.DEBUG,
                            format="[%(asctime)s %(threadName)s %(levelname)s]:%(message)s",
                            datefmt='%m-%d %H:%M:%S',
                            handlers=[logging.FileHandler("./log.log",mode="w"),logging.StreamHandler()])

@dataclass
class cve_from_request:
    _id:str = None
    cve_meta_info:str = None

@dataclass
class cve_data:
    data: List[cve_from_request]=field(default_factory=list)

def data_into_csv(data:cve_data):
        with open('MetaInfo.csv', 'w', newline='') as f:
            fieldnames = ['_id', 'cve_meta_info']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for payload in data.data:
                writer.writerow({'_id': payload._id, 'cve_meta_info': payload.cve_meta_info})

def get_cve_info(args:argparse.Namespace=None):
    base_url = "https://services.nvd.nist.gov/rest/json/cves/1.0?cpeMatchString=cpe:2.3"

    if args.type not in ["a","h","o"]:
        message = f"wrong --type argument {args.type}"
        raise ValueError(message)

    url = f"{base_url}:{args.type}:{args.vendor}:{args.product}:{args.version}"
    
    asyncio.get_event_loop().run_until_complete(searching(url))

async def request(url:str, index:int=0,delay:int=60):
    logging.info(f"request url:{url} with index:{index} ")
    
    start = "&startIndex=" + str(index)
    full_url = url + start

    async with aiohttp.ClientSession() as session:
        async with session.get(full_url) as response: 
            content_type = response.headers['content-type']
            logging.info(f"full url for get request: {full_url}")
            logging.info(f"status from response: {response.status}")
            logging.info(f"Content-type: {content_type}")
            
            if response.status == 403 and content_type == "text/html":
                await asyncio.sleep(delay)
                return await request(url,int(index),delay)
            else:
                result = await response.text()
                # logging.debug(result)
                return result

async def searching(url:str, elements:int=100, batch_page:int=3):

    total = totalResults(await request(url))

    curr_cve_data = cve_data()
    pages = ceil(int(total / elements))

    logging.info(f"all pages: {pages}")

    tasks = []
    count = 0
    logging.debug(f"{pages},{batch_page},{total},{elements}")

    for i in range(0,int(pages / batch_page)):
        for j in range(0,batch_page):
            logging.info(f"requesting page #{count+1}")
            tasks.append(request(url,count*elements))
            count+=1

    res = await asyncio.gather(*tasks)

    for i in range(0,count):
        logging.info(f"Response page #{i+1}")
        handle(res[i],curr_cve_data)
    data_into_csv(curr_cve_data)

def handle(text, payload_data:cve_data):
    if text == "ERROR":
        logging.error("Error 403, pass")
        payload_data.data.append(cve_from_request("ERROR", "403"))
    else:
        try:
            data = json.loads(text)
            logging.info(text)

            for cve in data["result"]["CVE_Items"]:
                try:
                    _id = cve["cve"]["CVE_data_meta"]["ID"]
                    cve_meta_info = cve["impact"]["baseMetricV3"]["cvssV3"]["vectorString"]
                    payload_data.data.append(cve_from_request(_id, cve_meta_info))

                except Exception as error :
                    logging.error("error")
        finally:
            logging.info("added")

def totalResults(text):
    if text == "ERROR":
        logging.error("Error 403, pass")
    else:
        data = json.loads(text)
        return data["totalResults"]



if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()

    parser.add_argument("--type", required=True, help="CPE type.")
    parser.add_argument("--product", default="*", help="CPE product.")
    parser.add_argument("--vendor", default="*", help="CPE vendor.")
    parser.add_argument("--version", default="*", help="CPE version.")

    args = parser.parse_args()
    print(args.type)

    get_cve_info(args)

