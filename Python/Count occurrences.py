# Count occurrences
# Given a sequence of integers and a query integer, count the number of times the query integer occurs in the sequence.

# Input
# First line contains the number of integers in the sequence, say n (n>0).

# Next n lines contain one integer each.

# Next 1 line contains one integer, which is the query integer.

# Output
# One line containing one integer, which is the number of times query integer occurs in the given sequence.

# Example
# Input:

# 5

# 2

# 3

# 4

# 3

# 5

# 3

# Output:

# 2

n=int(input())
l=[]
for i in range (n):
 m=int(input())
 l.append(m)
q=int(input())
count=0
for i in range(len(l)):
 if l[i]==q:
  count+=1
print(count)
 