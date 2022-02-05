# Number occurring maximum times
# Given a list of N integers sorted in ascending order, Please find the number which occurs 4 times in the array

# Input
# First number is N (the number of integers given) Followed by the N numbers

# Output
# Print the number which occurs 4 times. print -1 if such a number doesnt exist

# Example
# Input: 10

# 1

# 2

# 3

# 4

# 4

# 4

# 4

# 5

# 6

# 6

# Output: 4

n=int(input())
l=[]
for i in range(n):
 m=int(input())
 l.append(m)
count=1
for i in range(n-1):
 if l[i]==l[i+1]:
  count=count+1
 else:
  if count==4:
   res=(l[i-1])
   print(res)
  count=1
if count==4:
  res=l[n-1]
  print(res)
else:
  print(-1)
    

