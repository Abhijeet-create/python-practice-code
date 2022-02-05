#Perimeter of a Rectangle
#Given the length and breadth of a rectangle, compute and print its perimeter. If no such rectangle exists print 0.

#Input
#Two lines containing one integer each

#Output
#One line containing one integer

#Example
#Input:

#7

#3

#Output:

#20

l = int(input())
b = int(input())
if l > 0 and b > 0:
  print(int(2*(l+b)))
else:
  print(int(0))