#!/bin/python3

import math
import os
import random
import re
import sys
        
def calculate_max(arr):
    max_val = 0
    last_element=0
    for i in arr:
        current = i + last_element
        if current > max_val:
            max_val=current
        last_element=current
    return max_val

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    #O(m+n) time, O(n) memory
    #Update the array twice for each query
    #A positive number means increment all numbers from this index by number. 
        #A negative number means decrement all numbers by this number from this index going forward
        #Then go through and find max through a special function keeping track of the previous vals when incrementing or decrementing new vals.
    #we will only update the start index for where a range has started to increase and the index after the end index to mark where the range ends. 
    arr = [0]*n
    
    #O(m)
    for q in queries:
        #Note the qeury is 1 indexed
        
        #e.g. for n of 5 and q 2 4 3 -> 0 0 0 0 0 become 0 0 3 0 0 -3
        k=q[2]
        arr[q[0]-1] +=k
        
        #decrementing the first index out of the interval
        if(q[1]<n):
            arr[q[1]] -=k
    
    #O(n)
    max_val = calculate_max(arr)
    return max_val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
