# Enter your code here. Read input from STDIN. 

def median_sorted(data):
    #calc median on sorted data
    N = len(data)
    if (N%2 != 0):
        mid = int(N/2)
        return data[mid]
    else:
        mid_upper = int(N/2)
        mid_lower = mid_upper -1
        med = (data[mid_upper]+data[mid_lower])/2
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
    
    #print("l" + str(mid_l))
    #print("u" + str(mid_u))
    Q1 = median_sorted(x[:mid_l+1])
    Q2 = median_sorted(x)
    Q3 = median_sorted(x[mid_u:])
    return [Q1,Q2,Q3]

def create_data(n,elements,frequencies):
    #O(s) where s is sum of frequencies
    count = sum(frequencies)
    data = [None]*count
    
    j, current = 0, 0
    for i in range(0,n):
        ele = elements[i]
        freq = frequencies[i]
        current+=freq
        for k in range(j,current):
            data[k] = ele
        j = current
    return data

def interquartile_range(n,elements,frequencies):
    data = create_data(n, elements, frequencies)
    Q1, _, Q3 = calc_quartiles(len(data), data)
    return round(float(Q3-Q1),1)


if __name__ == "__main__":
    n = int(input())
    elements = input().split(' ')
    elements = [int(x) for x in elements]
    frequencies = input().split(' ')
    frequencies = [int(x) for x in frequencies]
    interquartile_range(n,elements,frequencies)
    
    print(interquartile_range(n,elements,frequencies))
