#!/bin/python3

'''A string is said to be a child of a another string if it can be formed by deleting 0 or more characters from the other string. Given two strings of equal length, what's the longest string that can be constructed such that it is a child of both?
For example, ABCD and ABDC have two children with maximum length 3, ABC and ABD. They can be formed by eliminating either the D or C from both strings. Note that we will not consider ABCD as a common child because we can't rearrange characters and ABCD != ABDC.'''

#All characters are upper case in the range ascii[A-Z]. They are also equal length.
#A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.



import math
import os
import random
import re
import sys

#Top down
def LCS_recursive(P, Q, n, m):
    #Finds length of LCS between P and Q
    #strings P, Q with lengths remaining of strings n and m respectively
    #first call is LCS_recursive(P, Q, len(P), len(Q))
    #O(2^(m+n)) time complexity O(1) space
    if(n==0 or m==0):
        #one of the strings is empty
        return 0
    elif( P[n-1]==Q[m-1]):
        #last char is same, look at lcs of remaining char
        return 1 + LCS_recursive(P, Q, n-1, m-1)
    else:
        return max(LCS_recursive(P, Q, n-1, m), LCS_recursive(P, Q, n, m-1))
    

#Top down

def LCS_topdown(P, Q, n, m, arr):
    #Finds length of LCS between P and Q
    #strings P, Q with lengths remaining of strings n and m respectively
    #first call is LCS_recursive(P, Q, len(P), len(Q))
    #arr is 2d array init to None
    #O(m*n) time complexity O(m*n) space
    
    if arr[n][m] is not None:
        return arr[n][m]
    
    if(n==0 or m==0):
        #one of the strings is empty
        result= 0
    elif( P[n-1]==Q[m-1]):
        #last char is same, look at lcs of remaining char
        result= 1 + LCS_topdown(P, Q, n-1, m-1, arr)
    else:
        result= max(LCS_topdown(P, Q, n-1, m, arr), LCS_topdown(P, Q, n, m-1, arr))
    arr[n][m] = result
    return result

def LCS_bottomup(P, Q):
    #Finds length of LCS between P and Q
    #strings P, Q with lengths remaining of strings n and m respectively
    #O(m*n) time, O(m*n) space
    #when visualizing can draw a table with one string as rows and one string as columns
    #cell [a][b] means lcs("a", "ab") = 1 it is cumulative in terms of the chars seen so far
    '''
      |""|a|b|c
    --
    "" 0 0 0 0
    __
    a  0 1 1 1
    __
    t  0 1 1 1
    __
    b. 0 1 2 2
    '''
    
    #want to remove last char in current string 1? move up a row i-1
    #want to remove last char in current string 2? move left one column j-1
    n = len(s1)
    m = len(s2)
    arr = [[None] * (m+1) for _ in range(n+1)]
    
    for i in range(n+1):
        for j in range(m+1):
            if (i==0 or j==0):
                arr[i][j]=0
            elif P[i-1] == Q[j-1]:
                arr[i][j] = 1 + arr[i-1][j-1]
            else:
                
                #max is too slow
                #arr[i][j] = max(arr[i-1][j], arr[i][j-1])
                if(arr[i-1][j] >= arr[i][j-1]):
                    arr[i][j] = arr[i-1][j]
                else:
                    arr[i][j] = arr[i][j-1]
                
    return arr[n][m]
            
def LCS_bottomup_optimized(P, Q):
    #Finds length of LCS between P and Q
    #strings P, Q with lengths remaining of strings n and m respectively
    #O(m*n) time, O(m) space (choose the string with shorter length)
    #when visualizing can draw a table with one string as rows and one string as columns
    
    #in this optimized version of bottomup dp we are only storing two rows of dp table
    #want to remove last char in current string 1? move up a row i-1
    #want to remove last char in current string 2? move left one column j-1
    
    n = len(s1)
    m = len(s2)
    arr1 = [0] * (m+1)
    arr2 = [0] * (m+1)
    
    #first row and col init to 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if P[i-1] == Q[j-1]:
                arr2[j] = 1 + arr1[j-1]
            else:
                #max is too slow
                if(arr1[j] >= arr2[j-1]):
                    arr2[j] = arr1[j]
                else:
                    arr2[j] = arr2[j-1]
        #end of row shift down
        arr1,arr2 = arr2,arr1
        
    #remember swap at the end
    return arr1[m]
    
# Complete the commonChild function below.
def commonChild(s1, s2):
    #want the largest common subsequence between the two strings
    #satisfies the two characteristics for dp
    #overlapping subproblems: can take longest common subsequence of substrings
    #optimal substructure property:  the longest common subsequence between two strings can be broken down into the longest common subsequence of either 1. the lcs two strings minus the last char if the last char is the same. 2. the max between the lcs of first string minus last char with second string and the lcs of the frst string with second string minus last char
    
    #n = len(s1)
    #m = len(s2)
    #col = m
    #row = n
    #arr = [[None] * (col+1) for _ in range(row+1)]
    if(len(s1)>len(s2)):
        lcs_len = LCS_bottomup_optimized(s1, s2)
    else:
        lcs_len = LCS_bottomup_optimized(s2, s1)
    #lcs_len = LCS_recursive(s1, s2, n, m)
    return lcs_len

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()
    
    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()