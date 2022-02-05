#Product & SUM
#Given an integer number N, return the difference between the product of its digits and the sum of its digits. Assume that the number N can never be negative number.

#Input
#One line containing the number N

#Output
#One line for the difference between product and sum

#Example
#Input: 234

#Output: 15

#Product of digits = 2 3 4 = 24 Sum of digits = 2 + 3 + 4 = 9 Result = 24 - 9 = 15

#Input: 4421

#Output: 21

#Product of digits = 4 4 2 * 1 = 32 Sum of digits = 4 + 4 + 2 + 1 = 11 Result = 32 - 11 = 21

N = int(input())
sum=0
pd=1
while N > 10:
   r=N%10
   sum=sum+r
   pd=pd*r
   N=N//10
sum=sum+N
pd=pd*N
print(int(pd-sum))