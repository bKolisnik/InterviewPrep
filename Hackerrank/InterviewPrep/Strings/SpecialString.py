#!/bin/python3

import math
import os
import random
import re
import sys
   
# Complete the substrCount function below.
def substrCount(n, s):
    #a string is special if all the characters are the same or all the characters except the middle one are the same
    #a special substring is any substring which satisfies either of the two requirements above
    #count the number of special substrings that can be formed from the string
    #solution in O(n) time complexity using O(n) memory
    
    #first major note is that for a char repeated k times e.g. aaa there are k(k+1)/2 valid substrings as you have a_0 + a_0a_1 a_0a_1a_2+ a_1 + a_1a_2 + a_2 for 6 valid substrings total num of substrings starting from each char are 3 + 2 + 1
    

    same_char_count = [0]*n
    
    #handle case 1 all repeated chars
    i=0
    ans =0
    #loop through the string and count the number of case 1 special substrings in O(n)
    while(i<n):
        j=i+1
        c=1
        while(j<n and s[i]==s[j]):
            j+=1
            c+=1
        ans+= (c*(c+1))//2
        same_char_count[i]=c
        i=j
    
    #handle case 2 repeated then middle then repeated O(n)
    #sliding window slides from index 1 to n-2 inclusive so second index to second last index
    for j in range(1,n-1):
        if(s[j]==s[j-1]):
            same_char_count[j] = same_char_count[j-1]
            
        #odd length substring which has a different middle element
        if(s[j-1]==s[j+1] and s[j-1]!= s[j]):
            #the length of the substrings that are valid is the minimum of the number of chars on one side or the other
            #e.g. aaaabaa the valid substrings are aabaa and aba
            ans+=min(same_char_count[j-1],same_char_count[j+1])
    
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
