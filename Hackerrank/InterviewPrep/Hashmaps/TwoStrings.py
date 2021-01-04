#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    #O(m + n) time where m is length s1, n is length s2. O(m) memory
    #for the strings to have a substring they must have at least one char in common
    s1_hm={}
    
    for char in s1:
        if char in s1_hm:
            s1_hm[char]+=1
        else:
            s1_hm[char]=1
            
    for char in s2:
        if char in s1_hm:
            return "YES"
    return "NO"
            
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
