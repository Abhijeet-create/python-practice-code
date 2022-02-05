#Square Sum
#Given a natural number n as input, find the sum of squares of first n natural numbers.

#Input
#One Integer, denoting n.

#Output
#One Integer, denoting the required sum.

#Example
#Input: 3

#Output: 14

#Explanation:

#1*1+2*2+3*3 = 14

n = int(input())
s = (n*(n+1)*((2*n)+1))/6
print(int(s)) 