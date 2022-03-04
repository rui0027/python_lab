#!/usr/bin/env python3

import sys
import re
import numpy
from numpy.random import choice
from collections import Counter
from text_stats import get_data

def generate_text(file,word,num):
    data=get_data(file)
    cur_word=word
    maxnum=int(num)
    msg=cur_word
    i=0
    for i in range(maxnum):
        data1=numpy.array(data)
        index=[i+1 for i in numpy.where(data1==cur_word)[0].tolist()] #index of successors
        successor=[data[i] for i in index]
        if len(successor)==0:
            msg=msg+" "+cur_word #stop generate if the word doesn's have any successor
            break
        else:
            sort_list=sorted([(x,successor.count(x)/len(successor)) for x in set(successor)],key=lambda x:x[1],reverse=True)
            cur_word=choice([x[0] for x in sort_list],1,[x[1] for x in sort_list])[0].tolist() #randomly select a successor by weights
            msg=str(msg)+" "+str(cur_word)
    return msg

if __name__ == "__main__":
    try:
        filename=sys.argv[1]
        word=sys.argv[2]
        num=sys.argv[3]
        f=open(filename)
        f.close()
    except IndexError:
        print("Please enter three arguments: filename, starting word, maxinum number of text.")
    except FileNotFoundError:
        print("The file does not exist!" )
    else:
        data=get_data(filename)
    print(f"{generate_text(filename,word,num)}")
