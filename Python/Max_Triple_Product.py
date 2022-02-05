# Max_Triple_Product
# Given an integer array, find three numbers whose product is maximum and output the maximum product.

# Input
# The first line denotes n, the size of the array. The next n lines denotes the n elements of the array.

# Output
# Output a single integer denoting the result.

# Example
# Input: 4

# 1

# 2

# 3

# 4

# Output: 24

# Note:
# The length of the given array will be in range [3,10^4] and all elements are in the range [-1000, 1000].

n=int(input())
l=[]
for i in range(n):
  l.append(int(input()))
l.sort()
print(l)
print(max(l[0]*l[1]*l[n -1],l[n-3]*l[n-2]*l[n-1]))