#!/usr/bin/env python3

import sys
import re
import os
from random import choices
from collections import Counter
from text_stats import get_data

def generate_text(file,word,num):
    data=get_data(file)
    cur_word=word
    maxnum=int(num)
    msg=cur_word
    i=0
    for i in range(maxnum):
        successor=[data[index+1] for index,item in enumerate(data) if item==cur_word]
        if len(successor)==0:
            msg=msg+" "+cur_word
            break
        else:
            count_list=dict(Counter(successor))
            cur_word=choices(list(count_list.keys()),list(count_list.values()),k=1)[0]
            msg=msg+" "+cur_word
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
