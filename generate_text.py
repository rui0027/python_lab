#!/usr/bin/env python3

import sys
import re
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
        
    cur_word=sys.argv[2]
    maxnum=sys.argv[3]
    msg=cur_word
    i=0
    for i in range(maxnum):
        data1=numpy.array(data)
        index=[i+1 for i in numpy.where(data1==cur_word)[0].tolist()]
        successor=[data[i] for i in index]
        if len(successor)==0:
            msg=msg+" "+cur_word
            break
        else:
            sort_list=sorted([(x,successor.count(x)/len(successor)) for x in set(successor)],key=lambda x:x[1],reverse=True)
            cur_word=choice([x[0] for x in sort_list],1,[x[1] for x in sort_list])[0].tolist()
            msg=str(msg)+" "+str(cur_word)
    print(msg)
