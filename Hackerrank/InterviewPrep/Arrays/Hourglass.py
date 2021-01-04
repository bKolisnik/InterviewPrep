#!/bin/python3

import math
import os
import random
import re
import sys

def get_hourglass_sum(arr,row,col):
    #get the sum of an hourglass centered at row, col
    #arr[row-1,col-1] + arr[row-1,col] + arr[row-1,col+1]
    #arr[row,col]
    #arr[row+1,col-1] + arr[row+1,col] + arr[row+1,col+1]
    
    hg_sum=0
    for i in range(-1,2):
        for j in range(-1,2):
            if(i==0) and ((j==-1)or(j==1)):
                continue
            hg_sum+=arr[row+i][col+j]
            
    return hg_sum
            

# Complete the hourglassSum function below.
def hourglassSum(arr):
    #O(N*M) time, O(1) space
    #print the maximum hourglass sum of the 16 hourglass sums
    rows = len(arr)
    cols = len(arr[0])
    
    hg_max = float('-inf')
    for i in range(1,rows-1):
        for j in range(1, cols-1):
            hg_sum = get_hourglass_sum(arr,i,j)
            print(hg_sum)
            if(hg_sum > hg_max):
                hg_max = hg_sum
    return hg_max
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
