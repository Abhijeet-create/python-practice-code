# Max by now
# You have been given n, denoting the number of input values. For each input, you have to print the maximum input taken so far.

# Note:
# You don't need to consider n in taking out this maximum.
# For the first input of n values, the max value will be that value itself.
# Input Format
# First line denotes the number of inputs n. The next n lines contains one integer each, denoting input values.

# Output Format
# There will be n lines in the output, containing one integer in each line, ith line denotes the maximum of the i inputs taken so far.

# Sample Input
# 5
# 3
# 2
# 5
# 10
# 8
# Sample Output
# 3
# 3
# 5
# 10
# 10
# Explanation
# The first line contains 5, denoting there will be 5 input values, in next 5 lines.
# Those inputs are 3,2,5,10,8.
# Corresponding to each of them, the maximum value received so far becomes 3,3,5,10,10.

# n=int(input())
# max=float('-inf')
# l=[]
# for i in range(n):
#  m=int(input())
#  l.append(m)
#  if l[i]>max:
#   print(l[i])
#   max=l[i]
#  elif max>l[i]:
#   print(max)
 
# n=int(input())
# maxx=float('-inf')
# for i in range(n):
#   val=int(input())
#   maxx= max(maxx, val)
#   print(maxx)



n=int(input())
l=[]
max=float('-inf')
for i in range(n):
 m=int(input())
 l.append(m)
 if l[i]>max:
  max=l[i]
 print(max) 