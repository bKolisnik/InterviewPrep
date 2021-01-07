# Enter your code here. Read input from STDIN. Print output to STDOUT
import math


#by CLT the sample mean of the random variables of the unknown distribution will approach N(mean, (1/n)(sd**2)) as n approaches infinity where sec param is var.
#the sd of that sampling dist is sqrt(1/n*sd**2) = (1/sqrt(n)) * sd
    

if __name__ == "__main__":
    #You have a sample of 100 values from a population with mean 500 and with standard deviation 80. Compute the interval that covers the middle 95% of the distribution of the sample mean; in other words, compute A and B such that P(A < X < B) = 0.95. Use the value of z=1.96. Note that  is the z-score.

    #https://en.wikipedia.org/wiki/Standard_score#Prediction_intervals
    #P(A < X < B) = P((A-mean)/sd < Z < (B-mean)/sd) = 0.95
    #and we know P(-z < Z < z) = 0.95 is true for z = 1.96
    #(A-mean)/sd = -z => that (A-mean) = -z*sd => A = mean -z*sd
    #thus A = mean -z*(sd)
    # B = mean + z*(sd) 
    
    #now this interval is for the sample mean so the mean of the sample mean sampling dist is population mean, and sd is (1/sqrt(n)) * sd thus var is (1/n)*sd**2
    
    n = float(input())
    
    #dont know the distribution but we do know the mean and sd
    mean = float(input())
    sd = float(input())
    prob = float(input())
    z = float(input())
    
    #sampling dist mean is same as pop mean
    sampling_dist_sd = sd/math.sqrt(n)
    print(round(mean - z*sampling_dist_sd, 2))
    print(round(mean + z*sampling_dist_sd, 2))