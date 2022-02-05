# Area and Perimeter of the Circle - Classes Practice Problems
# Design a class with has 2 methods. One which calculates area of the circle and one which calculates the circumference of a circle given the radius r. Please use the pi value as 3.14. For any infeasible radius r, please return the area and circumference as 0.0

# Your class should be named Circle. Method to get area should be named getArea. Method to get circumference should be named getCircumference.

# Input
# One line containing a floating point number denoting the radius r.

# Output
# 2 lines containing floating point numbers. First one containing the area of the circle. second line containing the circumference of the circle.

# Example
# Input:

# 5
# Output:

# 78.5
# 31.4
# First line in input is radius r which is 5. Area is 5*5*3.14 which is 78.5 which is the first line of the output. Circumference is 2*3.14*5 which is 31.4 which is the second line of the output.

class Circle():
 def __init__(self,r):
  Circle.pi=3.14
  self.radius=r

 def getArea(self):
   Area=(self.radius**2)*Circle.pi
   return Area

 def getCircumference(self):
   Circum=2*Circle.pi*self.radius
   return Circum

r=float(input())
c1=Circle(r)
if r<=0:
 print(float(0))
 print(float(0))
else:
 print(c1.getArea())
 print(c1.getCircumference())


 
  
