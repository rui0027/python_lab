#!/usr/bin/env python3

import re
import sys
import numpy
import os
from collections import Counter


def get_data(filename):
    with open(filename, "r",encoding='UTF-8') as f:
        data=list()
        for line in f:
            line_split=[x.lower() for x in re.split('[ ,.!?;:""''\n]+',line)]
            data.extend(list(filter(lambda x:x!="",line_split)))
    return data

def count_letters(data):
    letters={"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0,}
    for k,v in letters.items():
        letters[f"{k}"]=sum([x.count(f"{k}") for x in data])
    return sorted(letters.items(),key=lambda x:x[1],reverse=True)

def count_words(data):
    return len(data)

def count_unique(data):
    return len(set(data))

def common_words(data):
    words=sorted(Counter(data).items(),key=lambda x:x[1],reverse=True)[:5]
    for x in words:
        successor=[data[index+1] for index,item in enumerate(data) if item==x[0]]
        sort_list=sorted(Counter(successor).items(),key=lambda x:x[1],reverse=True)[:3]
        print(f"{x[0]} ({x[1]} occurrences)\n--{sort_list[0][0]},{sort_list[0][1]}\n--{sort_list[1][0]},{sort_list[1][1]}\n--{sort_list[2][0]},{sort_list[2][1]}")


class ArgError(Exception):
    def __init__(self,arg):
         self.arg=arg
class MissFileError(Exception):
    def __init__(self,arg):
         self.arg=arg



if __name__ == "__main__":
    try:
        input=sys.argv
        if len(input)!=2:
            raise ArgError(input)
        filename=sys.argv[1]
        if os.path.isfile(f'./{filename}')==False:
            raise MissFileError(filename)
    except ArgError:
        print("Please enter file name.")
    except MissFileError:
        print("The file does not exist!")
    else:
        data=get_data(filename)
        print(f"frequency of alphabetic letters:{count_letters(data)}")
        print(f"number of words:{count_words(data)}")
        print(f"number of unique words:{count_unique(data)}")
        print("five most commonly used words:")
        common_words(data)
