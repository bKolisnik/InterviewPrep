#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def check_geo_prog(one,two,three,r):
    if(two == r*one) and (three == r*two):
        return True

# Complete the countTriplets function below.
def countTripletsNaive(arr, r):
    #O(n^3) time to look through each triplet and check if its a geo prog
    n = len(arr)
    count=0
    
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if(check_geo_prog(arr[i],arr[j],arr[k],r)):
                    count+=1
    return count
    
def countTriplets(arr,r):
    #O(n) time complexity, O(n) memory
    #recall to be a triplet i<j<k
    #keep track of a left map with number of occurrences of each element to the left of the current element
    #keep track of a right map with the number of occurrences of each element to the right of the current element
    
    total_triplets=0

    #Construct hashmap in O(N), Counter is sublclass of dict
    hm_l = Counter()
    hm_r = Counter(arr)
    
    #process each element as if it is the midpoint is the geo prog aka ele j
    for ele in arr:
        count_left = 0
        count_right = 0
        
        #decrement the right hashmap by one as this is the current element
        hm_r[ele]-=1
        
        if(ele*r in hm_r):
            count_right=hm_r[ele*r]
        if(ele%r ==0):
            if(ele/r in hm_l):
                count_left = hm_l[ele/r]
        total_triplets+=count_left*count_right
        
        #add current element to left map
        if(ele in hm_l):
            hm_l[ele]+=1
        else:
            hm_l[ele]=1
        
    return total_triplets
            
        
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
