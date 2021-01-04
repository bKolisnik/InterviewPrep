#!/bin/python3

import math
import os
import random
import re
import sys

def calc_new_ind(index,d,N):
    #doing subtraction in the Ring Z_n where n is num elements in the array
    return (index-d)%N

# Complete the rotLeft function below.
def rotLeftOld(a, d):
    #O(N) time, O(N) space where N is len(a)
    #[1,2,3,4,5] -> [5,1,2,3,4] for d = 4 rotations
    #in eg above index 0 -> 1, 1 -> 2, 2-> 3, 3-> 4, 4 -> 0
    
    N = len(a)
    new_index = [calc_new_ind(i,d,N) for i in range(0,N)]
    
    rotated = [None]*N
    for count, ind in enumerate(new_index):
        rotated[ind] = a[count] 
    
    return rotated

def rotLeft(a, d):
    #O(N) time, O(1) space where N is len(a)
    #[1,2,3,4,5] -> [5,1,2,3,4] for d = 4 rotations
    #in eg above index 0 -> 1, 1 -> 2, 2-> 3, 3-> 4, 4 -> 0
    
    #using the fact that d<=n
    #if d > n need to use the other solution above
    return a[d:] + a[:d]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()