# Enter your code here. Read input from STDIN. Print output to STDOUT

def geometric_prob(n, p):
    #random variable, pmf is a function of n
    q = 1-p
    
    return (q**(n-1))*p

def geometric_cumulative(n, p):
    #cdf is a function of n, support is n=1,2,3,...
    #number of Bernoulli trials needed to get 1 success
    cumulative_prob = 0
    for i in range(1,n+1):
        cumulative_prob+=geometric_prob(i,p)
    
    return cumulative_prob
    
    
if __name__=="__main__":
    #what is the probability the first defect is found during the first 5 inspections
    #X~geometric(p)
    #P(X<=5)
    
    line = input()
    vals = line.split(' ')
    inspection = int(input())

    num = float(vals[0])
    denom = float(vals[1])
    p = num/denom
    
    print(round(geometric_cumulative(inspection,p),3))
    
