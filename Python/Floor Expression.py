# Floor Expression
# Given a positive integer n. Find the sum of product of x and y such that floor(n/x) = y .

# You just need to complete the given function (n is given as argument, and return required sum), in the template code. Don't worry about input and output.

# Input
# One integer, denoting n.

# Output
# One Integer, denoting the result.

# Example
# Input1:

# 5
# Output1:

# 21
# Explanation1:

# Following are the possible pairs of (x, y): (1, 5), (2, 2), (3, 1), (4, 1), (5, 1).
# So, 1*5 + 2*2 + 3*1 + 4*1 + 5*1 
#    = 5 + 4 + 3 + 4 + 5 
#    = 21.

def prod(n):
 sum=0
 for i in range(1,n+1):
  y=int(n/i)
  product=(y*i)
  sum+=product
 print(sum)
n= int(input())
prod(n)