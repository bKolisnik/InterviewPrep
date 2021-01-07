# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def normal_cumulative(mu,sd,x):
    scaled = (x-mu)/(sd*math.sqrt(2))
    return 0.5*(1+math.erf(scaled))
    
if __name__=="__main__":
    #let X~N(mu, sd)
    
    line = input()
    vals = line.split(' ')

    mu = float(vals[0])
    sd = float(vals[1])
    
    q1 = float(input())
    q2_1, q2_2 = list(map(int, input().rstrip().split()))
    
    #P(X<=19)
    print(round(normal_cumulative(mu, sd, q1),3))
    #P(20<=X<=22)
    print(round(normal_cumulative(mu, sd, q2_2)-normal_cumulative(mu, sd, q2_1),3))
    
