This file has answers to the multiple choice questions.

1. Basic Probability

In a single toss of 2 fair (evenly-weighted) six-sided dice, find the probability that their sum will be at most 9.

want P(X1+X2 <=9) where X1, X2 are discrete with pmf P(x_i) = {1/6} for i = 1..6

basically can construct a new pmf for their sum let Z = X1 + X2. then Z has pmf based on this table of outcomes (each element is sum of two outcomes for X1 and X2)

| sum | X2=1 | X2=2 | X2=3 | X2=4 | X2=5 | X2=6 |
| -- | -- | -- | -- | -- | -- |
| X1=1 | 2 | 3 | 4 | 5 | 6 | 7 |
| X2=2 | 3 | 4 | 5 | 6 | 7 | 8 |
| X1=3 | 4 | 5 | 6 | 7 | 8 | 9 |
| X1=4 | 5 | 6 | 7 | 8 | 9 | 10 |
| X1=5 | 6 | 7 | 8 | 9 | 10 | 11 |
| X1=6 | 7 | 8 | 9 | 10 | 11 | 12 |

//Full pmf can be explicitly written as
P(Z=z) = {1/36, if z=2, 
           2/36 if z=3,
           3/36, if z=4 
           etc}

P(Z>9) = 6/36 = 1/6 so P(Z<=9) = 1-1/6 = 5/6


2. More dice

In a single toss of 2 fair (evenly-weighted) six-sided dice, find the probability that the values rolled by each die will be different and the two dice have a sum of 6.

Using the previous sum table we can see that out of 36 possible outcomes for the two dice 5 outcomes were 6 and of those outcomes (1, 5), (2, 4), (4, 2) and (5, 1) were different. Thus P(Z = 6 | X1!=X2) = 4/36 = 1/9

3. Compound event probability

There are 3 urns labeled X, Y, and Z.

Urn X contains 4 red balls and 3 black balls.
Urn Y contains 5 red balls and 4 black balls.
Urn Z contains 4 red balls and 4 black balls.

One ball is drawn from each of the 3 urns. What is the probability that, of the 3 balls drawn, 2 are red and 1 is black? Let P(rrb) be shortform for P(X1=r, X2= r, X3 = b). Drawing from each urn is independent of the  previous urns.
P(X1 =x)  = {3/7, if x=b
            4/7 if x=r}

P(X2 =x) = {4/9, if x=b
            5/9, if x=r}

P(X3 =x) = {1/2, if x=b
            1/2, if x=r}

let event A be the set of outcomes where there are two r and one b

P(A) = P(rrb) + P(rbr) +P(brr) = 
(4/7)*(5/9)*(1/2) + (4/7)*(4/9)*(1/2) + (3/7)*(5/9)*(1/2)  = 17/42

4. Conditional probability

Suppose a family has 2 children, one of which is a boy. What is the probability that both children are boys? 

Assuming the probabilities are independent and identical.

Let X1, X2 be iid (independent and identically distributed) ~ (sampled) from f where f is the pmf p(x) = P(X=x) = {1/2, if x = b and 1/2, if x = g}

Need to decompose the joint as P(X2=b|X1=b, X2=b)*P(X1=b, X2=b), also note P(X2=b|X1=b, X2=b) = 1

P(X1=b, X2=b| X2=b) = P(X2=b|X1=b, X2=b)*P(X1=b, X2=b) / P(X2 = b) = 1*(1/4)/(3/4) = 1/3

check out the bayesian analysis section https://en.wikipedia.org/wiki/Boy_or_Girl_paradox

