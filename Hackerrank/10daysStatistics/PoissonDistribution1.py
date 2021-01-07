# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def poisson_prob(lamb, x):
    num = (lamb**x)*(math.e**(-lamb))
    denom = factorial(x)
    return num/denom
    
    
if __name__=="__main__":
    #what is the probability that X~Poisson(2.5) takes on value 5?
    #P(X=5)
    
    lamb = float(input())
    val = float(input())
    
    print(round(poisson_prob(lamb,val),3))