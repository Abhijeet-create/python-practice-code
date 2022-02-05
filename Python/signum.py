# signum
# A signum function returns 1 for numbers greater than zero and -1 for numbers less than zero and 0 for an input of 0. Write a signum implementation that takes a float N and returns an integer.

# Input
# One line containing a decimal number.

# N

# Output
# One integer, denoting the output value.

# Example
# Input:

# -0.87

# Output:

# -1

def sig(num):
 if num<0:
  return -1
 elif num>0:
  return 1
 else:
  return 0
num=float(input())
print(sig(num))
