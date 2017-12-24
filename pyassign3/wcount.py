#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Yang Zhengji"
__pkuid__  = "1700011817"
__email__  = "1700011817@pku.edu.cn"
"""

import sys
from urllib.request import urlopen
from functools import reduce

def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """

    docstr=lines
    dic={}
    docstr=docstr.replace("\r\n"," ")
    docstr=list(docstr.lower())
    docstr=filter(lambda x : (x.isalpha() or x is " " or x is "'" or x is "-" or x is"_")  ,docstr)
    docstr=reduce(lambda x,y: x+y,docstr)
    docstr=docstr.replace("-"," ")
    docstr=docstr.replace("_"," ")
    list_0=docstr.split(" ")
    list_0=filter(lambda x:(x is not " " and x is not ""),list_0)
    for items in list_0:
        if items in dic:
            dic[items] +=1
        else:
            dic[items] =1
    x=sorted(dic.items(),key =lambda item:item[1],reverse=True)
    for i in range(topn):
        print(x[i][0],x[i][1])

    
    pass

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
