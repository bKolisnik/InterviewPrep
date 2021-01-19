#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col

def dfs_region(grid, visited, row, col):
    #start a dfs from cell i,j that is marked with a 1
    component_size=0
    stack = deque()
    stack.append(Cell(row, col))
    n = len(grid)
    m = len(grid[0])
    
    while(stack):
        cell = stack.pop()
        if(not visited[cell.row][cell.col]):
            visited[cell.row][cell.col] = True
            component_size+=1
    
        #checking if neighbors and not visited
        for i in range(cell.row-1, cell.row+2):
            for j in range(cell.col-1, cell.col+2):
                #if indexes are inbounds
                if (i >= 0) and (i < n) and (j >=0) and (j < m) and not (i==cell.row and j==cell.col):
                    if (not visited[i][j]) and (grid[i][j]==1):
                        stack.append(Cell(i,j))
                        
                        
    return component_size
# Complete the maxRegion function below.
def maxRegion(grid):
    
    #create 2d visited array
    visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
    max_component_size = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not visited[i][j] and (grid[i][j]==1):
                component_size = dfs_region(grid, visited, i, j)
                max_component_size = max(max_component_size, component_size)
    return max_component_size

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()