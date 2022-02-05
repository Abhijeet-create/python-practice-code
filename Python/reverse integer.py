#reverse integer
#Given an integer, reverse digits of an integer

#Input
#1 line containing the integer to reverse

#Output
#1 line containing the reversed integer

#Example
#Input: 123

#Output: 321

#Input: 120

#Output: 21 because starting 0 can be removed

#Input: -123

#Output: -321


n=int(input())
rev=0
if n<0:
  n=n*-1  
  while n > 0:
    r=n%10
    rev=(rev*10+r)
    n=n//10
  print(-rev)
else: 
   while n > 0:
    r=n%10
    rev=(rev*10+r)
    n=n//10
   print(rev)  
 
        