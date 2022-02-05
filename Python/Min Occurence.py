# Min Occurence
# You have been given n integer values. Lets say the given values are a1, a2, a3, a4 ...

# You need to find the number of occurence of the first value in the given inputs.

# Input Format:
# First line denotes n, the number of inputs. The next n lines contains one integer in each line.

# Output Format:
# One integer denoting the result, as mentioned above.

# Example:
# Input:

# 5
# 10
# 20
# 30
# 40
# 10
# Output:

# 2
# Explanation:

# From the given 5 integers, the number of occurence of the first number (10) is 2.
n=int(input())
i=0
arr=[]
count=0
while i <n:
 m=int(input())
 arr.append(m)
 i+=1
for i in range(len(arr)):
 if arr[0]==arr[i]:
  count+=1
print(count)
 