#Area of rectangle
#Given length and breadth of a rectangle, compute the area of the rectangle.

#Input
#Two lines containing one integer each. First line contains the length and second line contains the breadth.

#Output
#One line containing one integer, which is the area of the given rectangle.

#Print 0 if no such rectangle exists.

#Example
#Input:

#5

#3

#Output:

#15

l = int(input())
b = int(input())
area = l*b
if l > 0 and b > 0:
 print(int(area))
else:
 print(int(0))