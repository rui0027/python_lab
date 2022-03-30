#!/usr/bin/env python3

import sys
import re
import os
import numpy as np
from random import choices
from text_stats import get_data

def generate_text(file,word,num):
    data=get_data(file)
    cur_word=word
    maxnum=int(num)
    msg=cur_word
    successor_list={x:{} for x in np.unique(data)}
    for index,item in enumerate(data):
        if index<len(data)-1:
            successor=data[index+1]
        if successor in successor_list[item].keys():
            successor_list[item][successor]+=1
        else:
            successor_list[item][successor]=1
    i=0
    for i in range(maxnum):
        if any(successor_list[cur_word].keys()):
            cur_word=choices(list(successor_list[cur_word].keys()),list(successor_list[cur_word].values()),k=1)[0]
            msg=msg+" "+cur_word
        else:
            msg=msg+" "+cur_word
            break
    return msg

class ArgsError(Exception):
    def __init__(self,arg):
         self.arg=arg
class MissFileError(Exception):
    def __init__(self,arg):
         self.arg=arg

if __name__ == "__main__":
    try:
        input=sys.argv
        if len(input)!=4:
            raise ArgsError(input)
        filename,word,num=sys.argv[1:4]
        if os.path.isfile(f'./{filename}')==False:
            raise MissFileError(filename)
    except ArgsError:
        print("Please enter arguments: filename, starting word, maxinum number of text.")
    except MissFileError:
        print("The file does not exist!" )
    else:
        data=get_data(filename)
    print(f"{generate_text(filename,word,num)}")
