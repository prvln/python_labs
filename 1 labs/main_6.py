import argparse
import json
from operator import ge
from sys import exc_info


def get_storage(_print=True):
    with open("./storage.data","r",encoding="utf-8") as file:

        try:
            content = json.load(file)
        except Exception as e:
            print("get_storage error: ",e)
            content = dict()
        finally:
            if _print:
                print(content)
            else: 
                return content

def get_value(key:str) -> str:
    content = get_storage(_print=False)

    try:
        values = content[key]
        print(str(values).replace("[",'').replace("]",'').replace("\'",''))
    except KeyError:
        print("there is no such key in storage! You can add it by command: storage --key key_name --value value_name ")
    except Exception as e :
        print(e)
    
    
def add_value(key:str,value:str):
    content = get_storage(_print=False)
    keys = content.keys()
    
    if key in keys:
        content[key].append(value)
    else:
        content[key] = [value]
    
    with open("./storage.data","w",encoding="utf-8") as file:
        json.dump(content,file,indent=4)
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Key-value storage")
    parser.add_argument(
        "-k", "--key", type=str, dest="key", help="Argument for key")
    parser.add_argument(
        "-v","--value",type=str,dest="value",help="Argument for key")

    args = parser.parse_args()
    if all([args.key != None , args.value != None]):
        add_value(args.key,args.value)
    elif args.key != None and args.value == None:
        get_value(args.key)
