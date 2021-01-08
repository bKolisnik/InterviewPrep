# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def spearman_rank_correlation(n, x, y):
    #need to create rank of x and y, using the question constraint they contain unique values
    #O(nlogn)
    #create dict where key is the element of the array and the value is the index of the sorted order
    sorted_x = dict((x_i,i+1) for i, x_i in enumerate(sorted(x)))
    #each element of rank is the ordering of the original array x
    rank_x = [sorted_x[i] for i in x]
    sorted_y = dict((y_i,i+1) for i, y_i in enumerate(sorted(y)))
    rank_y = [sorted_y[i] for i in y]
    
    di_2 = 0
    for i in range(n):
        di_2+=(rank_x[i]-rank_y[i])**2
    
    return 1- 6*(di_2)/(n*(n**2 - 1))
    
    
if __name__ == "__main__":
    #Spearman's Rank Correlation Coefficient
    #using the fact that the data is unqiue so each value only appears once.
    #the rank of a data point is its index if the data was sorted in ascending order
    #spearman correlation is the pearson correlation between the ranks of x and y
    
    n = int(input())
    
    x = list(map(float,input().strip().split()))
    y = list(map(float,input().strip().split()))
    print(round(spearman_rank_correlation(n, x, y), 3))