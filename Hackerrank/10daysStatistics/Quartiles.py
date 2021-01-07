# Enter your code here. Read input from STDIN. Print output to STDOUT


def median_sorted(data):
    #calc median on sorted data
    N = len(data)
    if (N%2 != 0):
        mid = int(N/2)
        return data[mid]
    else:
        mid_upper = int(N/2)
        mid_lower = mid_upper -1
        med = (data[mid_upper]+data[mid_lower])//2
        return med


def calc_quartiles(n, x):
    #O(nlogn) time complexity and O(n) memory
    x.sort(reverse=False)
    
    if(n%2!=0):
        mid_u = n//2 +1
        mid_l = n//2 - 1
    else:
        mid_u = n//2
        mid_l = n//2 -1
    
    Q1 = median_sorted(x[:mid_l+1])
    Q2 = median_sorted(x)
    Q3 = median_sorted(x[mid_u:])
    return [Q1,Q2,Q3]
        

    

if __name__ == "__main__":
    n = int(input())
    data = input().split(' ')
    data = [int(x) for x in data]
    
    quarts = calc_quartiles(n,data)
    print(str(quarts[0]))
    print(str(quarts[1]))
    print(str(quarts[2]))
