# Factorial: Iterative
# Description
# Write a program that computes the factorial of a given integer. Your implementation should be iterative in nature. Factorial of an integer n is defined as Factorial(n) = 1*2*3*....*(n-2)*(n-1)*n. Factorial(0) is defined as 1. Factorial of a negative integer is undefined.

# Input format
# One line containing an integer n.

# Output format
# One line containing the factorial of n.

# Sample input
# 5
# Sample output
# 120
# Explanation
# Factorial of 5 is 1*2*3*4*5 which is 120.

# Sample input
# -4
# Sample output
# undefined
# Explanation
# Factorial of a negative integer is undefined.

n=int(input())
i=n
fac=1
while i>0:
 fac*=i
 i-=1
if n>0:
 print(fac)
if n==0:
 print(1)
if n<0:
 print("undefined")    
 