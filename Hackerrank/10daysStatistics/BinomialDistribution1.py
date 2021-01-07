# Enter your code here. Read input from STDIN. Print output to STDOUT

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def binomial_prob(n, x, p):
    q = 1-p
    n_C_x = factorial(n)/(factorial(x)*factorial(n-x))
    p_X_x = n_C_x*(p**x)*(q**(n-x))
    return p_X_x

def boys_proportion(boys, girls):
    #If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys? Need to hardcode these values as not passed as input
    
    #odds is defined as o = p/(1-p) => that p = o/(1+o)
    odds = boys/girls
    p_1 = odds/(1+odds)
    
    #3<=x<=6
    prob = binomial_prob(6,3,p_1)
    prob+= binomial_prob(6,4,p_1)
    prob+= binomial_prob(6,5,p_1)
    prob+= binomial_prob(6,6,p_1)
    return round(prob, 3)
    

if __name__=="__main__":
    
    line = input()
    vals = line.split(' ')
    #the ratios of boys to girls
    boys = float(vals[0])
    girls = float(vals[1])
    print(boys_proportion(boys,girls))
