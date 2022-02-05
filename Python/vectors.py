#Vectors
#Given two force vectors, find out whether they are parallel, perpendicular or neither. Let the first vector be A = a1 i +a2 j + a3 k and the second vector be B = b1 i + b2 j + b3 k.

#A.B = a1 x b1 + a2 x b2 + a3 x b3

#A x B = (a2 x b3 - a3 x b2) i - (a1 x b3 - b1 x a3) j + (a1 x b2 - a2 x b1) k

#|A|2 = a12 + a22 + a32

#If A.B = 0, then A and B are perpendicular.

#If |A X B| = 0, then A and B are parallel.

#Input
#First line contains three space seperate values denoting, a1, a2, a3 respectively. Second line contains three space seperate values denoting, b1, b2, b3 respectively.

#Output
#Print 1 if they are parallel to each other, 2 if they are perpendicular to each other or 0 otherwise.

#Example
#Input1:

#3 2 1
#6 4 2
#Output1:

#1
#Explanation:

#|A X B| = o

a, b, c = map(int, input().split())
x, y, z = map(int, input().split())
X = int((a*x)+(b*y)+(c*z))
Y = int(((b*z)-(c*y))**2-((a*z)-(x*c))**2+((a*y)-(b*x))**2)
if X == 0:
    print(2)
elif Y == 0:
    print(1)   
else:
    print(0)