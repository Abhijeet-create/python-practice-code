# Best Team
# There are three groups of students(all groups have equal no. of students) who are appearing for a team selection process. From each group we have to choose exactly one student so that we have a team of 3 students. Every student has a skill value associated with them. Let the team chosen have three players whose skills are given by (Tmin<=Tmid<=Tmax). A teams balance score is given as |Tmax-Tmid|+|Tmin-Tmid|. A team with lower balance score is said to be more balanced. Can you find the most balanced team?

# Note:- |x| is asolute value of x

# Input
# Input contains of 3 lines, first line is an array of skill values of first group, second line is an array containing skill value of second group and similarly for the third group.

# 1<=length of the any group<=100000

# skill value>=1

# Output
# Print the best balance score possible (i.e-least balance score amongst all the possibilities)

# Example
# Input:

# 1 5 2 3

# 2 4 1 8

# 6 6 5 9

# Output:

# 1

# explaination

# choose 5 from G1, 4 from G2 and 5 from G3, then the score is |5-4|+|5-5| which is 1 which is also the minimum.


L1= [int(x) for x in input().split()]
L2= [int(x) for x in input().split()]
L3= [int(x) for x in input().split()]
arr=[]
for i in range(len(L1)):
 for j in range(len(L1)):
  arr.append(abs(L1[i]-L2[j]))
pos1=min(arr)
arr2=[]
for i in range(len(L3)):
  for j in range(len(L3)):
   arr2.append(abs(L2[i]-L3[i]))
pos2=min(arr2)
print(pos1+pos2)
    
