# Given a positive integer, find out the sum of its digits.
# 54
# How can I get 4 from 54?
# What is the reminder if we divide 54 by 10? We will get 4.
# Modulus operator. Denoted by %.
# a % b gives us the reminder when we divide a by b
# a // b - will give you the quotient when we divide a by b

# Get the right most digit - % 10
# Get the next right most digit

# 9584
# 9584 % 10 --> 4
# 9584 // 10 --> 958
# 958 % 10 --> 8
# 958 // 10 --> 95
# 95 % 10 --> 5
# 95 // 10 --> 9

num = int(input())
sumOfDigits = 0
while num > 10:
    reminder = num % 10
    sumOfDigits = sumOfDigits + reminder
    num = num // 10
sumOfDigits = sumOfDigits + num