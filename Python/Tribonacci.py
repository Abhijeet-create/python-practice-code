# Tribonacci
# Nth Tribonacci number is defined as:

# Tribonacci[N] = Tribonacci[N-1] + Tribonacci[N-2] + Tribonacci[N-3]

# Tribonacci[0] = Tribonacci[1] = 0
# Tribonacci[2] = 1
# Given an integer N, print the Nth Tribonacci Number.

# Input
# One integer, denoting N.

# Output
# One Integer, denoting the result.

# Example
# Input1:

# 5
# Output1:

# 2
# Explanation:

# Series will be: 0,0,1,1,2...


def trib(n):
 first=0
 second=0
 third=1

 for i in range(3,n):
  curr=third+second+first
  first=second
  second=third
  third=curr
 print(curr)

n=int(input())
trib(n)