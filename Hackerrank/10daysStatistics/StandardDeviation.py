# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def mean(data):
    #O(n) time, O(1) memory
    mu = 0
    for i in data:
        mu += i
    mu /= len(data)
    return mu

def standard_deviation(N, x):
    mu = mean(x)
    var_num = 0
    for x_i in x:
        var_num+=(x_i - mu)**2
    var = var_num/N
    std_dev = math.sqrt(var)
    return round(std_dev, 1)
    
    
if __name__=="__main__":
    N = int(input())
    x = input().split(' ')
    x = [int(i) for i in x]
    print(standard_deviation(N, x))