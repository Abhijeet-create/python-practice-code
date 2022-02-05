# Find if given number is prime
# Find if the given integer is prime number.

# Input
# FirstLine contains an interger specifying no. of test cases. Each line contains integers specifying value of number in each test case.

# Output
# Yes if number is prime. No is not for each testcase.

# Example
# Input: 3

# 2

# 4

# 5

# Output: Yes

# No

# Yes
n=int(input())
for i in range(n):
 m=int(input())
 if m==2 or m==3 or m==5:
    print("Yes")
 elif m%2==0 or m%3==0 or m%5==0:
    print("No")
 else:
    print("Yes")

