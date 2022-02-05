# Output
# One Integer, denoting the N-th term in the series 1, 3, 6, 10, 15, 21....

# Example
# Input1:

# 4
# Output1:

# 10
# Input2:

# 3
# Output2:

# 6

n=int(input())
sum=0
for i in range(1,n+1):
 sum+=i
print(sum)