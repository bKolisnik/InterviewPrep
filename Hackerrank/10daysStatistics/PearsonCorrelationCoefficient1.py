# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def mean(data):
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
    return std_dev

def pearson_correlation(n, x, y):
    mu_x, sd_x = mean(x), standard_deviation(n, x)
    mu_y, sd_y = mean(y), standard_deviation(n, y)
    
    num=0
    for i in range(n):
        num+=(x[i]-mu_x)*(y[i]-mu_y)
        
    return num/(n*sd_x*sd_y)
    
if __name__ == "__main__":
    n = int(input())
    
    x = list(map(float,input().strip().split()))
    y = list(map(float,input().strip().split()))

    print(round(pearson_correlation(n, x, y), 3))
    