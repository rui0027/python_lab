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
        f=open("111.txt")
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
        
"""
In addition, you should provide a brief answer to the following questions:

[ ] In what way did you "clean up" or divide up the text into words (in the program; the text files should be left
unaffected)? This does not have to be perfect in any sense, but it should at least avoid counting "lord",
"Lord" and "lord." as different words.

For each line of the text file, first we divided the line into words by using re.split() with some common seperators and converted all words into lower case. 
Because some marks at the end of a line are treated as seperators, the words contain many useless "" in it. So we used a filter to select the real words.
Then we merged the words into a empty list 'data' by extend() while reading the file.

[ ] Which data structures have you used (such as lists, tuples, dictionaries, sets, ...)? Why does that choice
make sense? You do not have to do any extensive research on the topics, or try to find exotic modern data
structures, but you should reflect on which of the standard data types (or variants thereof) make sense. If
you have tried some other solution and updated your code later on, feel free to discuss the effects!

We used list to save data because list is more flexible than tuples and has many built-in functions. 
In the defined functions, sometimes we use dictionary to save the result of some object and the numbers of counts, because it's easier to sort paired data.
Sometimes we need to change list into array so that we can use numpy.where to make the step of getting indexs of selected items easier.
"""
