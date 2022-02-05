# Given a person's age and diabetes status, determine if the person is eligible for covid vaccine.
# Input: Two lines. First line contains an integer, which is the age of the person. Second line contains a string. "Yes" if the person is diabetic, "No" if the person is not diabetic.
# Output: One line containing a string. "Eligible" if the person is eligible. "Not eligible" if the person is not eligible.

# Test case 1
# Input:
#   54
#   No
# Ouput: Not eligible

# Test case 2
# Input:
#   67
#   Yes
# Ouput: Eligible

# 1. Read age
# 2. Reade diabetes status
# 3. If age is greater than 60, then print Eligible
# 4. Otherwise if age is greater than 45 and the person is diabetic, then print Eligible
# 5. Otherwise print Not eligible

age = int(input())
diabeticStatus = input()
if age > 60:
    print("Eligible")
elif age > 45 and diabeticStatus == "Yes":
    print("Eligible")
else:
    print("Not eligible")