# Sum of Multiples
# Write a function which takes a list L of positive intergers and a positive integer N(N > 0) and returns the sum of all the intergers of the list L which are multiples of N.

# Input
# Write a function sum_of_multiples which takes a list and an integer

# Output
# integer

# Example
# Input:

# [1,2,3,4,5,6,7], 3 inputs for function

# Output:

# 9

def sum_of_multiples(n,l):
 sum=0   
 for i in range(len(l)):
   if l[i]%n==0:
    sum+=l[i]
 print(sum)

l=[int(x) for x in input().split()]
n=int(input())
sum_of_multiples(n,l)
