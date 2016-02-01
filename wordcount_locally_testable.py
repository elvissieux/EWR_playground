#!/usr/bin/python
import sys 
import re 

#change with a test file here
filepath = "your_path_here"

def main(argv): 
    print argv
    pattern = re.compile("[a-zA-Z][a-zA-Z0-9]*")
    #switch between local and hadoop cluster prod (launch with any argument for local test)
    for line in [open(filepath), sys.stdin, ][len(argv)==1]:
        for word in pattern.findall(line):
            print "LongValueSum:" + word.lower() + "\t" + "1" 


if __name__ == "__main__": 
    main(sys.argv) 
    
    
