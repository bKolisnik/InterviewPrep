#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the makeAnagram function below.
def makeAnagramOld(a, b):
    #O(a + b) time where a is number of chars in str a and b is number of chars in str b.
    #O(v) memory where v is size of vocabulary
    #Minimum number of deletions to make the two strings anagrams.
    hm_a = Counter(a)
    hm_b = Counter(b)
    deletions = 0
    for key, value_a in hm_a.items():
        if key in hm_b:
            value_b = hm_b[key]
            diff = abs(value_a-value_b)
            deletions+=diff
            del hm_b[key]
        else:
            deletions+=value_a
    #Anything still in b was not in a so it must be deleted
    for key, value_b in hm_b.items():
        deletions+=value_b
    return deletions
    
def makeAnagram(a, b):
    hm_a = Counter(a)
    hm_b = Counter(b)
    hm_a.subtract(hm_b)
    #generator expression
    return sum(abs(i) for i in hm_a.values())
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
