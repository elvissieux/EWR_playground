#!/usr/bin/python
import sys 
import re 

filepath = "/media/t0135444/DATA/wordcount/input/0010"

def main(argv): 
    print argv
    pattern = re.compile("[a-zA-Z][a-zA-Z0-9]*")
    for line in [open(filepath), sys.stdin, ][len(argv)==1]:
        for word in pattern.findall(line):
            print "LongValueSum:" + word.lower() + "\t" + "1" 


if __name__ == "__main__": 
    main(sys.argv) 
    
    
