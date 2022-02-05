# Difference of sum of Even Odd Index numbers
# Write a function which takes a list of positive integers and returns the difference of sum of numbers and even and odd index positions.

# Your function should take the list, sum all the numbers which are located at even index poistion of list and sum all the which are located at odd index poistion of list and subtract odd postion sum from even position sum.

# you should name the function as difference_sum_even_odd_index and it should take a list.

# Index of the list starts from 0.

# If list has only one element, then sum of odd = 0

# Input
# list of positive intergers

# Output
# Integer

# Example
# Input:

# [1,2,3,4,5,6]

# Output:

# -3
def difference_sum_even_odd_index(l):
 se=0
 so=0
 if len(l)<1:
  so=0      
 for i in range(len(l)):
  if i%2==0:
   se+=l[i]
  elif i%2==1:
   so+=l[i]
 diff=(se-so)
 print(diff)
l=[int(x) for x in input().split()]
difference_sum_even_odd_index(l)




