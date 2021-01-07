# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def normal_cumulative(mu,sd,x):
    scaled = (x-mu)/(sd*math.sqrt(2))
    return 0.5*(1+math.erf(scaled))
    
if __name__=="__main__":
    #let X~N(mu, sd) be the random variable representing the distribution of the grades in the class
    
    
    line = input()
    vals = line.split(' ')

    mu = float(vals[0])
    sd = float(vals[1])
    
    q1 = float(input())
    fail = float(input())
    
    
    #P(X>80)
    a1 = (1 - normal_cumulative(mu, sd, q1))*100
    a2 = (1- normal_cumulative(mu, sd, fail))*100
    a3 = (normal_cumulative(mu, sd, fail))*100
    print(round(a1,2))
    #P(X>=60) = 1- P(X<=60)
    print(round(a2,2))
    #P(X<=60)
    print(round(a3,2))