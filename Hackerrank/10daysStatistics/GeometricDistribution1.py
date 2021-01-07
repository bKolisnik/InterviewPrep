# Enter your code here. Read input from STDIN. Print output to STDOUT

def geometric_prob(n, p):
    #random variable, pmf is a function of n
    q = 1-p
    
    return (q**(n-1))*p
    
    
if __name__=="__main__":
    
    line = input()
    vals = line.split(' ')
    inspection = int(input())

    num = float(vals[0])
    denom = float(vals[1])
    p = num/denom
    
    print(round(geometric_prob(inspection,p),3))
    
