#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    #all character counts must be the same (call this c) we can delete one character at one index. ssaabbbdd is valid, so is aabbd.
    #O(n) time complexity, O(n) memory complexity
    
    #Build hashmap of counts in O(n)
    hm_counts = Counter(s)
    
    #for first example above 2: 3, 3: 1, second example 2: 2, 1: 1
    hm_frequency = Counter(hm_counts.values())
    #this hashmap should only have two keys for the two frequencies
    if(len(hm_frequency)==1):
        return "YES"
    if(len(hm_frequency)==2):
        #two cases it can either be one above or it can be one
        #O(1)
        min_key = min(hm_frequency.keys())
        max_key = max(hm_frequency.keys())
        diff = max_key-min_key
        if diff==1 and hm_frequency[max_key]==1:
            return "YES"
        elif min_key==1 and hm_frequency[min_key]==1:
            return "YES"
        else:
            return "NO"
        
    else:
        return "NO"
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()