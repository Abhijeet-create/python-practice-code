# Swap Function
# Given two integers a and b, you need to write a function to swap the their values.

# Note: Write a function, and do the swapping operation in the function only.

# Input
# First line contains an integer denoting a

# Second line contains an integer, denoting b

# Output
# First line denoting the value of a after swapping.

# Second line denoting the value of b after swapping.

# Example
# Input:

# 30
# 110
# Output:

# 110
# 30


def swap(a,b):
 a, b=b, a
 print(a)
 print(b)
a=int(input())
b=int(input())
swap(a,b)

# def swap(a,b):
#  a, b=b, a
#  return a, b
# a=int(input())
# b=int(input())
# a,b=swap(a,b)
# print(a)
# print(b)