# Problem: Given the age of a person, determine if he/she is eligible for vote.
# Input format: One line containing an integer
# Output format: If the person is eligible, print Yes otherwise print No

# Test case 1
# Input: 20
# Output: Yes

# Test case 2
# Input: 60
# Output: Yes

# If the age is greater than 18, the person is eligible. Otherwise, the person is not eligible.

# 1. Read age from the user
# 2. If age is greater than 18, print Yes
# 3. If age is not greater than 18, print No

age = int(input())
if age > 18:
    print("Yes")
else:
    print("No")