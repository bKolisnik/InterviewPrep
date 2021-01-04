#!/bin/python3

import math
import os
import random
import re
import sys

def swap(arr,i,j):
    #swap the array elements at these two locations
    arr[i], arr[j] = arr[j], arr[i]

# Complete the minimumSwaps function below.
def minimumSwapsBest(arr):
    #O(n) time (looks at each element at most twice), O(1) memory
    #only for arrays with no duplicates and consecutive integers
    N=len(arr)
    swaps=0
    for i in range(N):
        element = arr[i]-1
        while (element) != i:
            swap(arr,i,element)
            swaps+=1
            element = arr[i]-1
            
    return swaps
            
#Intended solution from hackerrank, more memory but follows the examples
def minimumSwaps(arr):
    #O(n) time, O(n) memory
    #for each cycle need to do len(cyc) - 1 swaps
    #thus summing the len -1 of each cycle will give us total number of swaps
    #if a element isnt in a cycle swapping it with elements in the cycle does not help
    
    N=len(arr)
    visited = [0]*N
    swaps=0
    
    for i in range(N):
        if(visited[i]==0):
            index = i
            final_spot = arr[i]-1
            length_cyc = 1
            visited[i]=1
            while(final_spot!=i):
                visited[final_spot] = 1
                index = final_spot
                final_spot = arr[final_spot] -1
                length_cyc+=1
            swaps+=length_cyc-1
            
    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()