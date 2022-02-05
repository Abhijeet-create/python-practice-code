# Matrix 101
# You have been given a matrix (2D array) of size n x m (n rows and m columns).

# You need to find the sum of all odd numbers in the given matrix.

# Input
# The first line contains two integers denoting n and m respectively. The next line n lines contains m space seperated integers each, denoting the elements of the given matrix.

# Output
# One Integer, denoting the required sum.

# Example
# Input1:

# 3 4
# 1 2 3 4
# 5 6 7 8
# 9 0 5 3
# Output1:

# 33
# Explanation:

# matrix =   [[1, 2, 3, 4],
#             [5, 6, 7, 8],
#             [9, 0, 5, 3]]

# Sum of all odd elements = 1 + 3 + 5 + 7 + 9 + 5 + 3 = 33

n,m=map(int, input().split())
#arr=[[int(x) for x in input().split()] for in range(n)] can also be done like this
arr=[]
summ=0
for i in range(n):
 arr.append([int(x) for x in input().split()])
for i in range(n):
 for j in range(m):
  if (arr[i][j]%2!=0):
    summ+=arr[i][j]
print(summ)
