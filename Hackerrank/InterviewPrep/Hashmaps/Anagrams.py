#!/bin/python3

import math
import os
import random
import re
import sys

#anagrams are any strings of the same length with the same set of chars any order
#Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

first_26_primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]

def create_hash(string):
    #O(n)
    #want all anagrams to correspond to the same hash
    #by fundamental theorem of arithmetic all positive integers > 1 are prime or can be represented as a product of prime numbers
    #e.g. 1200 = 2^4*3*5^2
    
    hash_key = 1
    for char in string:
        hash_key*=first_26_primes[ord(char)-ord('a')]
    return hash_key
    
    #idea is to map each unique char in our character set to a different prime
    

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    #for 4 matching anagram substrings there are 6 anagram pairs
    #k choose 2 anagram pairs where k is number of anagram substrings
    
    #find number of pairs of substrings that are anagrams of eachother
    #there are n^2 substrings of a string, bcr must be O(n^2)
    #O(n^3logn) time, O(n^2) memory to sort each anagram
    
    #O(n^3) time, O(n^2) memory can take advantage of the fact that only lowercase letters a-z in string by creating unique hash in O(n)
    
    anagram_counts = {}
    count = 0
    
    #generate all substrings
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            
            #to sort each was O(nlogn) to map multiple anagrams to same key
            #key = ''.join(sorted(list(s[i:j])))
            
            #my main optimization is to create the unique hash in O(n) where all anagrams corespond to same hash
            key = create_hash(s[i:j])
            
            if key in anagram_counts:
                count+=anagram_counts[key]
                anagram_counts[key]+=1
            else:
                
                anagram_counts[key]=1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
