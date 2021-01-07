# Enter your code here. Read input from STDIN. Print output to STDOUT

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def binomial_prob(n, p, x):
    q = 1-p
    n_C_x = factorial(n)/(factorial(x)*factorial(n-x))
    p_X_x = n_C_x*(p**x)*(q**(n-x))
    return p_X_x
    
def binomial_cumulative(n,p,x):
    
    cumulative_prob = 0
    for i in range(0,x+1):
        cumulative_prob+=binomial_prob(n, p, i)
    return cumulative_prob
    
if __name__=="__main__":
    
    #defining a reject as a "success"
    #let X_i~B(p=0.12)
    
    
    line = input()
    vals = line.split(' ')
    #the ratios of boys to girls
    p = float(vals[0])/100
    n = float(vals[1])
    #P(X<=2)
    print(round(binomial_cumulative(n,p,2),3))
    #P(X>=2) = P(X<=10) - P(X<=1) = 1 - P(X<=1)
    print(round(binomial_cumulative(n,p,10) - binomial_cumulative(n,p,1),3))
    
