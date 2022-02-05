# Amazing Sum
# You have been given n integer values. Lets say the given values are a1, a2, a3, a4 ...

# If the sum of two consecutive input values is greater than 100, then the given values have amazing sum

# Input Format:
# First line denotes n, the number of inputs. The next n lines contains one integer in each line.

# Output Format:
# One string, either True or False, denoting whether the given values has amazing sum or not.

# Example:
# Input:

# 5
# 10
# 20
# 30
# 40
# 50
# Output:

# False
# Explanation:

# The maximum sum of two consecutive values here is 90, which is not greater than 100, so the answer is False.

n=int(input())
arr=[]
for i in range(n):
 m= int(input())
 arr.append(m)
i=0
while i < n-1:
 sum=arr[i]+arr[i+1]
 i+=1
 if sum > 100:
  print(True)
  break
if sum <= 100:
 print(False)