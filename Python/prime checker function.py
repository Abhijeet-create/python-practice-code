# prime checker function
# Write a function that takes a positive integer n and returns either True or False. It should return True when n is prime and False whenn` is not prime.

# Input
# One positive integer N

# Output
# One Boolean, denoting whether or not the given N is prime

# Example
# You have fill in a function. That function takes N as input

# Input:

# def is_prime(number)

# Output:

# Function should return True or False


def is_prime(n):
 if n>1:
  if n==2:
   print("True")
  else:       
   for i in range(2,n):
    if n%i==0:
     print("False")      
     break
   else:
    print("True")
 else:
  print("False")
n=int(input())
is_prime(n)
