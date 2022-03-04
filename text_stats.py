#!/usr/bin/env python3

import re
import sys
from collections import Counter

def get_data(filename):
    with open(f"{filename}", "r",encoding='UTF-8') as f:
        globals()['data']=list()
        for line in f:
            line_split=[x.lower() for x in re.split('[ ,.!?;:""''\n]+',line)]
            data.extend(list(filter(lambda x:x!="",line_split)))

if __name__ == "__main__":
    try:
        filename=sys.argv[1]
        f=open(f"{filename}")
        f.close()
    except IndexError:
        print("Please enter file name.")
    except FileNotFoundError:
        print("The file does not exist!" )
    else:
        get_data(filename)
        
def count_letters():
    letters={"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0,}
    for k,v in letters.items():
        letters[f"{k}"]=sum([x.count(f"{k}") for x in data])
    return sorted(letters.items(),key=lambda x:x[1],reverse=True)
        
def count_words():
    return len(data)
  
def count_unique():
    return len(set(data))

def common_words():
    words=sorted(Counter(data).items(),key=lambda x:x[1],reverse=True)[:5]
    data1=numpy.array(data)
    for x in words:
        index=[i+1 for i in numpy.where(data1==x[0])[0].tolist()]
        successor=[data[i] for i in index]
        sort_list=sorted([(x,successor.count(x)) for x in set(successor)],key=lambda x:x[1],reverse=True)[0:3]
        print(f"{x[0]} ({x[1]} occurrences)\n--{sort_list[0][0]},{sort_list[0][1]}\n--{sort_list[1][0]},{sort_list[1][1]}\n--{sort_list[2][0]},{sort_list[2][1]}")

