#Palindrome Number
#Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward

#Input
#1 containing integer

#Output
#1 line containing Boolean value

#Example
#Input: 121

#Output: True

#Input: 10

#Output: False

n=int(input())
m=n
rev=0
while n > 0:
     r=n%10
     rev=(rev*10+r)
     n=n//10
if rev==m:
   print(True)
else:
   print(False)        