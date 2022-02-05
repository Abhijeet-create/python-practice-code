# area and perimeter of rectangle -- Classes Practice Problems
# Design a class which has 2 methods. One which computes the Area of the Rectangle. The other computes the Perimeter of the Rectangle. You should be able to pass the length l and width w while creating the object for the class. For all infeasible values of length l and width w, print area and perimeter as 0

# Your class should be named as Rectangle. Method to get area should be named as rectangle_area. Method to get perimeter should be named as rectangle_perimeter.

# Input
# First line contains an integer for the length l Second line contains an integer for the width w

# Output
# Two lines containing integers. First line containing the Area of the Rectangle Second line containing the Perimeter of the Rectangle

# Example
# Input:

# 3
# 2
# Output:

# 6
# 10
# First line is 3 representing the length. Second line is 2 representing the width. Area is 3*2 which is 6 as represented in the first line of the output. Perimeter is 2*(3 + 2) which is 10 as represented in the second line of the output.

class Rectangle():
 def __init__(self,l,w):
  self.length=l
  self.width=w
 
 def rectangle_area(self):
  area=self.length*self.width
  return area

 def rectangle_perimeter(self):
  per=2*(self.length+self.width)
  return per
l=int(input())
w=int(input())
r1=Rectangle(l,w)
if l<=0 or w <=0:
 print(0)
 print(0)
else:
 print(r1.rectangle_area())
 print(r1.rectangle_perimeter())
