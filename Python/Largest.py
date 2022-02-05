# Largest
# Given an array A of size n.

# The task is to complete the largestElement function. It should return the largest element present in the given array.

# Note:
# DO NOT use any inbuilt function.
# Array may contain duplicate elements.
# Input
# First line contains one integer, denoting n. The next line contains n space seperated integers, denoting the elements of the given array.

# Output
# One Integer, denoting the result.

# Example
# Input1:

# 5
# 1 8 7 56 90
# Output1:

# 90
# Explanation1:

# The largest element of given array [1, 8, 7, 56, 90] is 90.

def largest(l):
 maxx=float('-inf')
 for i in range(len(l)):
  if l[i]>maxx:
    maxx=l[i]
 print(maxx)

n=int(input())
lt=[int(x) for x in input().split()]
largest(lt)

