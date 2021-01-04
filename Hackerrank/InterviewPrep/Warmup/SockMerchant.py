#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def init_sock_occ(ar):
    hm = {}
    for i in ar:
        if i in hm:
            hm[i]+=1
        else:
            hm[i]=1
    return hm
def sockMerchant(n, ar):
    #O(n) time, #O(n) mem
    sock_occ = init_sock_occ(ar)
    total_pairs = 0
    for sock, count in sock_occ.items():
        pairs = count//2
        total_pairs+=pairs
    return total_pairs
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()