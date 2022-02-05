# Extreme Product
# You have been given n integer values. You have to find their extreme product.

# Extreme product is defined as the product of the two extreme values in the given input, that is maximum and minimum.

# Input Format:
# First line denotes n, the number of inputs. The next n lines contains one integer in each line.

# Output Format:
# One integer denoting the extreme product of the given n values.

# Example:
# Input:

# 5
# 10
# 20
# 30
# 40
# 50
# Output:

# 500
# Explanation:

# From the given 5 integers, the maximum is 50, and the minimum is 10. So the extreme product is 10x50 = 500.

n=int(input())
l=[]
for i in range(n):
 m=int(input())
 l.append(m)
max=l[0]
min=l[0]
for i in range(n):
  if l[i]>max:
    max=l[i]
  if l[i]<min:
    min=l[i]
print(min*max)