#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    #O(n) time, O(1) space
    #Using the fact that you can only bribe at most 2 people a person cannot be more than 2 indexes ahead of their original position
    #1 2 5 3 7 8 6 4
    #3 got bibed once, 6 got bribed 3 times, 4 got bribed 4 times
    bribes = 0
    max_val = 0
    
    #ints to keep track of the next 3 stickers if they were in sorted order
    E_first = 1
    E_second = 2
    E_third = 3
    
    for index, ele in enumerate(q):
        if(ele==E_first):
            #shift up by 1
            E_first=E_second
            E_second=E_third
            E_third+=1
        elif(ele==E_second):
            bribes+=1
            E_second=E_third
            E_third+=1
        elif(ele==E_third):
            bribes+=2
            E_third+=1
        else:
            #difference is > 2 indexes to the left
            print("Too chaotic")
            return
        
        
        #you can only move to the right if you have been bribed
        #countnumber of places to the right you are of where you are supposed to be
        
    print(bribes)
    
    
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)