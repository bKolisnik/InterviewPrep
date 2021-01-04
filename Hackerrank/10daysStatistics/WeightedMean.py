# Enter your code here. Read input from STDIN. Print output to STDOUT

def weighted_mean(data,weights):
    #data and weights will be same size
    N = len(data)
    
    num = 0
    denom = 0
    
    for i in range(N):
        num += data[i]*weights[i]
        denom += weights[i]
        
    return round(num/denom,1)

if __name__ == "__main__":
    num = input()
    data = input().split(' ')
    data = [int(x) for x in data]
    
    weights = input().split(' ')
    weights = [int(w) for w in weights]
    print(weighted_mean(data,weights))
    