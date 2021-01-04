#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter, defaultdict


class Response:
    def __init__(self):
        
        #key is the integer, value is the count for that integer
        self.data = defaultdict(lambda: 0)
        #inverse of data, keys are the count and values are the number of ints with this count
        self.counts = defaultdict(lambda: 0)
        self.counts[1] = 0
        
    def add_value(self, val):
        if val in self.data:
            count = self.data[val]
            self.data[val]+=1
            self.counts[count]-=1
            self.counts[count+1]+=1
        else:
            self.data[val]=1
            self.counts[1]+=1
    def remove_value(self,val):
        if val in self.data and self.data[val]>0:
            count = self.data[val]
            self.data[val]-=1
            self.counts[count]-=1
            if count != 1:
                self.counts[count-1]+=1
    def check_exact_freq(self, freq):
        if freq in self.counts and self.counts[freq] > 0:
            return 1
        else:
            return 0
            
        
def init_results(queries):
    m = 0
    for q in queries:
        if q[0] == 3:
            m+=1
    results = [None]*m
    return results

# Complete the freqQuery function below.
def freqQuery(queries):
    resp = Response()
    results = init_results(queries)

    m=0
    for q in queries:
        #performs each op in O(1) amoritized time for all queries. thus O(m) time. O(n) memory where n is the range of values the integers can take on. (not including the O(m) memory needed to store query 3 responses)
        if q[0]==1:
            resp.add_value(q[1])
        elif q[0]==2:
            resp.remove_value(q[1])
        else:
            res = resp.check_exact_freq(q[1])
            results[m]=res
            m+=1
    return results
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
