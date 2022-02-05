# Special Range
# Given a range, as [m, n] both inclusive, print all non-negative integers in the range.

# Input
# First line contains an integer which is starting value of range, say m

# Second line contains an integer which is ending value of range, say n

# Output
# Print all non-negative integers in that range. One integer per line.

# If no such integers exist, print -1.

# Example
# Input:

# -5

# 4

# Output:

# 0

# 1

# 2

# 3

# 4



n= int(input())
m= int(input())
i=n
while i<=m:
  if i >=0:
   print(i)
  i=i+1
if n<0 and m<0 : 
 print(-1)
    
    

