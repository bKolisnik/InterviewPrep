#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

from collections import deque

class Departure:
    def __init__(self,stack):
        #first_step an indicator of direction, currently on a mountain or valley
        self.first_step = ""
        self.stack = stack
        self.valleys = 0
    def take_step(self,step):
        if(len(self.stack)==0):
            self.first_step=step
            self.stack.append(step)
        elif(step==self.first_step):
            self.stack.append(step)
        else:
            #Returning closer to sealevel, if mountain this is desc
            self.stack.pop()
            if (len(self.stack)==0):
                if(self.first_step=='D'):
                    self.valleys+=1
                self.first_step=""
                    
def countingValleysOld(steps, path):
    # Write your code here
    stack = deque()
    dep = Departure(stack)
    
    for char in path:
        dep.take_step(char)
    return dep.valleys

#Don't need the stack, can be done with constant memory.
def countingValleys(steps, path):
    # Write your code here
    #O(n) time, O(1) mem
    alt = 0
    valleys=0
    for char in path:
        if(char=="U"):
            alt+=1
        elif(char=="D"):
            alt-=1
        if(char=="U") and (alt==0):
            valleys+=1
            
    return valleys
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()