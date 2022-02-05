# Monotonic Array
# Given as array containing 
# n
#  integers, verify if the array is Monotonic.

# An array is called monotonic if it is either monotone increasing or monotone decreasing. An array A is monotone increasing if for all i <= j, A[i] <= A[j]. An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

# Input
# First line contains 
# n
# , number of elements in the array.

# Next n lines contains an integer in each line.

# Output
# Print True if given integers are Monotonic

# Print False if given integers are not Monotonic

# Example
# Input:

# 5

# 3

# 12

# 34

# 34

# 56

# Output:

# True

n=int(input())
arr=[]
asc=0
des=0
for i in range(n):
 arr.append(int(input()))
for i in range(n-1):
 if arr[i]>arr[i+1]:
   asc=1
 if arr[i]<arr[i+1]:
   des=1
if(asc==0 or des==0):
    print("True")
else:
    print("False")