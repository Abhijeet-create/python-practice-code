# print with index
# You are given a function print_with_index that takes a number and a string to print a message. You are also given a list that contains n strings. Write a function named printer that uses print_with_index to print the list elements with their indices.

# Input
# First line contains n denoting the number of strings given, 0 <= n <= 100

# This is followed by n lines, each denoting one string element of the lit

# Output
# The output must contain n lines.

# Each line starts with the index value of the element, followed by a space then the element itself

# Example
# Input: 4

# hello

# cat

# dog

# raining

# Output:

# 0 hello

# 1 cat

# 2 dog

# 3 raining

# The first line is 4, denoting that there are 4 elements in the list. Th eelements are hello, cat, dog, raining. The output should be 4 lines. Each line has the index first, followed by the element itself. Index of hello is 0, index of cat is 1 and so on:

def print_with_index(n,str):
 print(n , str)
def printer(n,l):
 for i in range(n):
  print_with_index(i,l[i])
n= int(input())
l=[]
for i in range(n):
  s=input()
  l.append(s)
printer(n,l)