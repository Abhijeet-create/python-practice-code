# Car
# Define a class named Car, which should have the name and model as the properties. You don't need to worry about input/output and object of the class. The given template will take care of it.

# The input will contain the name and model. Their default values should be Audi and A4 respectively.

# Input
# First line contains an integer, either 1 or -1. If the first line is 1, then:

# One line containing two space seperated values, denoting name and model respectively.
# Output
# Print name and model in newline each.

# Example
# Input1:

# 1
# Ford C4
# Output1:

# Ford
# C4
# Input2:

# -1
# Output2:

# Audi
# A4

class Car:
  def __init__(self, n, m):
    self.name=n
    self.model=m
    print(self.name)
    print(self.model)

x=int(input())
if x==1:
 n, m=input().split()
 c1=Car(n,m)
elif x==-1:
 default=Car('Audi','A4')
