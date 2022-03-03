#!/usr/bin/env python3

import sys
import re
from collections import Counter

with open(f"{sys.argv[1]}", "r",encoding='UTF-8') as f:
    data=list()
    for line in f:
        line_split=[x.lower() for x in re.split('[ ,.!?;:""''\n]+',line)]
        data.extend(list(filter(lambda x:x!="",line_split)))
        
