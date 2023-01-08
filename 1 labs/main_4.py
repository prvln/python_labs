def files(name:str) -> dict:
    with open(name,"r",encoding="UTF-8") as f:
        word = dict()
        for lines in f:
            words = lines.split()
            if words not in words:
                words[lines] = 0
            else:
                words[lines] +=1
        
    return words