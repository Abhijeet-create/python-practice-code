# problem : You are given a cubic dice with 6 faces. All the individual 
# faces have a number printed on them. The numbers are in the range of 
# 1 to 6, like any ordinary dice. You will be provided the number on the 
# top face of this cube, your task is to guess the number on the opposite 
# face of the cube.
# Constraints:
# 1 <= N <= 6
# Input
# One integer, denoting the number on the top face.

# Output
# One Integer, denoting the number on the opposite face.

# Example
# Input1:

# 6
# Output1:

# 1
# Input2:

# 2
# Output2:

# 5

num = int(input())
if num == int(1):
   print(int(6))
elif num == int(2):
   print(int(5))
elif num == int(3):
   print(int(4))
elif num == int(4):
   print(int(3))
elif num == int(5):
   print(int(2))
else:
   print(int(1))
    