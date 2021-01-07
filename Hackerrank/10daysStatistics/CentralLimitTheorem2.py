# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def normal_cumulative(mu,sd,x):
    scaled = (x-mu)/(sd*math.sqrt(2))
    return 0.5*(1+math.erf(scaled))

def prob_all_tickets(max_tickets, n, mean, sd):
    #by CLT the sum of the random variables of the unknown distribution will approach N(n*mean, n*(sd**2)) as n approaches infinity where sec param is var.
    #the sd of that sampling dist is sqrt(n*sd**2) = sqrt(n)*sd
    #we want the prob that this sum is less than or equal to 250
    return normal_cumulative(n*mean, math.sqrt(n)*sd, max_tickets)
    

if __name__ == "__main__":
    #The number of tickets purchased by each student for the University X vs. University Y football game follows a distribution that has a mean of 2.4 and a standard deviation of 2.0.

    #A few hours before the game starts, 100 eager students line up to purchase last-minute tickets. If there are only 250 tickets left, what is the probability that all 100 students will be able to purchase tickets?

    num_tickets = float(input())
    num_students = float(input())
    #dont know the distribution of num tickets bought per person but we do know the mean and sd
    mean = float(input())
    sd = float(input())

    print(round(prob_all_tickets(num_tickets, num_students, mean, sd), 4))
