# Growth
# You have been given n integer values. Lets say the given values are a1, a2, a3, a4 ...

# If the average of all these input values is greater than 100, then the given values are excellent.

# Input Format:
# First line denotes n, the number of inputs. The next n lines contains one integer in each line.

# Output Format:
# One string, either Excellent! or Not Excellent!, denoting whether the given values are excellent or not.

# Example:
# Input:

# 5
# 10
# 20
# 30
# 40
# 50
# Output:

# Not Excellent!
# Explanation:

# The average of these values is 30, which is less than 100. Hence, they are not excellent.


n= int(input())
l=[]
sum=0
for i in range(n):
 m=int(input())
 l.append(m)
 sum+=l[i]
if (sum/n) > 100:
 print("Excellent!")
else:
 print("Not Excellent!")

