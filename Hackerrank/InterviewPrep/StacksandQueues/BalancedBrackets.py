#Complete the function isBalanced in the editor below. It must return a string: YES if the sequence is balanced or NO if it is not.
#isBalanced has the following parameter(s):
#s: a string of brackets
#All chracters in the sequences ∈ { {, }, (, ), [, ] }.

#The first line contains a single integer n, the number of strings.
#Each of the next n lines contains a single string s, a sequence of brackets.

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

# Complete the isBalanced function below.
def isBalanced(s):
    #O(n) time, O(n) space where n = len(s))
    #if a closing bracket it needs to be the complement of the bracket on top of the stack
    if len(s)%2!=0:
        return "NO"
    
    d = deque()
    for bracket in s:
        if bracket == "{" or bracket == "[" or bracket == "(":
            d.append(bracket)
        else:
            if len(d) == 0:
                return "NO"
            top_element = d.pop()
            if bracket == "}" and top_element != "{":
                return "NO"
            elif bracket == "]" and top_element != "[":
                return "NO"
            elif bracket == ")" and top_element != "(":
                return "NO"
    
    if len(d)==0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
