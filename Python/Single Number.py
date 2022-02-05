# Single Number
# Given a list of N integers, every element appears twice except for one. Find that single one.

# Input
# First number is N (the number of integers given) Followed by the N numbers

# Output
# One line containing the output integer

# Example
# Input: 3

# 2

# 2

# 1

# Output: 1

# Input: 5

# 2

# 2

# 1

# 1

# 3

# Output: 3

# n = int(input())
# l=[]
# for i in range(n):
#  m=int(input())
#  l.append(m)
# for i in range(len(l)):
#  for j in range(len(l)):
#   if l[i]==l[j]:
#     continue
#   else:
#    out=l[i]
# print(out)
   
n = int(input())
l=[]
for i in range(n):
 m=int(input())
 l.append(m)
for i in range(len(l)):
 occurence=0
 for j in range(len(l)):
  if l[i]==l[j]:
    occurence+=1
 if occurence==1:
  print(l[i])


# n = int(input())
# l=[]
# for i in range(n):
#  l.append(int(input()))
# occurence=0
# for i in range(n):
#   occurence=occurence^l[i]      # ^ sign is for xor // n^n=0  and n^0=n
# print(occurence)                # e.g  2^2=0  and 2^0=2