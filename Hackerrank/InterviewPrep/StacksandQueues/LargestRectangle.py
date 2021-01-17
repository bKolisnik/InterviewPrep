#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#There are a number of buildings in a certain two-dimensional landscape. Each building has a height, given by h[i]. If you join k adjacent buildings, they will form a solid rectangle of area k x min(h[i],h[i+1],....,h[i+k-1]).
#For example, the heights array h=[3,2,3]. A rectangle of height h=2 and length k=3 can be constructed within the boundaries. The area formed is h x k = 2 x 3 = 6.

#can brute force in O(n^2) time O(1) space by analyzing all viable subrectangles similar to checking all substrings. We can proceed right from each starting point and when the next rectangle is smaller than starting point height we can end the rectnagle and compare it with max area until we have iterated through each start point. 

#python deque indexed access is O(1) at both ends but O(n) in the middle.

def subrectangle(max_area, curr_pos, heights, positions):
    temp_height = heights.pop()
    temp_position = positions.pop()
    temp_area = temp_height*(curr_pos-temp_position)
    max_area = max(max_area, temp_area)
    return temp_position, max_area

# Complete the largestRectangle function below.
#Keep track of rectangles opening and shutting using a stack
def largestRectangle(h):
    #Iterative solution in O(n) time, O(n) space
    
    #stacks to keep track of positions of rectangles (where they started) and heights of rectangles
    positions = deque()
    heights = deque()
    largest = 0
    temp_height = 0
    max_area=float("-inf")
    
    
    for i in range(len(h)):
        curr_h = h[i]
        
        #Check top of stack if the current element is larger open a new rectangle
        if not heights or (curr_h > heights[len(heights)-1]):
            positions.append(i)
            heights.append(curr_h)
        elif curr_h < heights[len(heights)-1]:
            while(len(heights) > 0 and heights[len(heights)-1]>curr_h):
                temp_position, max_area = subrectangle(max_area,i,heights,positions)
                #dont lose track of where current rectangle started. This rectangle starts at the furthest back index which will the last popped temp_position
                #that is last element that was same size or bigger than this element.
            
            heights.append(curr_h)
            positions.append(temp_position)
    
    #calculate remaining areas for rectangles still in stack
    while(len(heights)>0):
         temp_position, max_area = subrectangle(max_area,len(h),heights,positions)
        
    return max_area
            
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
