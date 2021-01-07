# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def normal_cumulative(mu,sd,x):
    scaled = (x-mu)/(sd*math.sqrt(2))
    return 0.5*(1+math.erf(scaled))

def prob_eleveator_safe(max_weight, n, mean, sd):
    #by CLT the sum of the random variables of the unknown distribution will approach N(n*mean, n*(sd**2)) as n approaches infinity where sec param is var.
    #the sd of that sampling dist is sqrt(n*sd**2) = sqrt(n)*sd
    #we want the prob that this sum is less than 9800
    return normal_cumulative(n*mean, math.sqrt(n)*sd, max_weight)
    

if __name__ == "__main__":
    #A large elevator can transport a maximum of 9800 pounds. Suppose a load of cargo containing 49 boxes must be transported via the elevator. 
    #The box weight of this type of cargo follows a distribution with a mean of mu = 205 pounds and a standard deviation of sd = 15 pounds. 
    #Based on this information, what is the probability that all 49 boxes can be safely loaded into the freight elevator and transported?

    #What is the probability that the sum of the weight of the 49 boxes <= 9800 pounds. 

    max_weight = float(input())
    number_boxes = float(input())
    #dont know the distribution of weight for boxes but we do know the mean and sd
    mean = float(input())
    sd = float(input())

    print(round(prob_eleveator_safe(max_weight, number_boxes, mean, sd), 4))
