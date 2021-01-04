# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

class Mode:
    def __init__(self):
        self.number = 0
        self.occurs = 0
    def set_mode(self,key,value):
        self.number = key
        self.occurs = value
        
def mean(data):
    #O(n) time, O(1) memory
    mu = 0
    for i in data:
        mu += i
    mu /= len(data)
    return round(mu,1)

def init_hm(data):
    hm = {}
    for i in data:
        if(i in hm):
            hm[i] +=1
        else:
            hm[i]=1
    return hm
def mode(data):
    #O(n) time #O(n) memory
    hm = init_hm(data)
    mode = Mode()
    for key, value in hm.items():
        if mode.occurs < value:
            mode.set_mode(key,value)
        elif mode.occurs == value and mode.number > key:
            mode.set_mode(key,value)
    return mode.number

def median(data):
    #O(nlogn) time complexity, O(1) memeory
    data = sorted(data,reverse=False)
    N = len(data)
    if (N%2)!=0:
        mid = int(N/2)
        return data[mid]
    else:
        mid_upper = int(N/2)
        mid_lower = mid_upper -1
        med = round((data[mid_upper]+data[mid_lower])/2,1)
        return med
            
if __name__ == "__main__":
    num = input()
    data = input().split(' ')
    data = [int(x) for x in data]
    print(mean(data))
    print(median(data))
    print(mode(data))