# Enter your code here. Read input from STDIN. Print output to STDOUT
    
def Expectation_C_A(lamb):
    #recall E[g(X)] = sum_over_x g(x)p(x)
    #by linearity the constants can be pulled out
    #E[X^2] = E[X]^2 + Var[X] = lambda^2 + lambda
    return 160 + 40*(lamb+lamb**2)

def Expectation_C_B(lamb):
    #recall E[g(X)] = sum_over_x g(x)p(x)
    #by linearity the constants can be pulled out
    #E[X^2] = E[X]^2 + Var[X] = lambda^2 + lambda
    return 128 + 40*(lamb+lamb**2)
    
if __name__=="__main__":
    #The manager of a industrial plant is planning to buy a machine of either type A or type B. For each day’s operation:

#The number of repairs, X, that machine A needs is a Poisson random variable with mean 0.88. The daily cost of operating A is C_A = 160+40X^2.
#The number of repairs, Y, that machine B needs is a Poisson random variable with mean 1.55. The daily cost of operating B is C_B = 128 + 40Y^2. Machines maintained nightly to operate like new each day. Find expected daily cost for each machine.

#Note for poisson dist the mean and var are both lamb so E[X^2] = E[X]^2 + Var[X] = lambda^2 + lambda
    
    lambs = input().split(' ')
    lamb_A, lamb_B = float(lambs[0]), float(lambs[1])
    
    print(round(Expectation_C_A(lamb_A),3))
    print(round(Expectation_C_B(lamb_B),3))