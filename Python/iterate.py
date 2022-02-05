#Input Format:
#First line denotes n.

#Output Format:
#Print the desired result. One integer in one line.

#Example:
#Input:

#5
#Output:

#5
#10
#15
#20
#25
#Explanation:

#5, 10, 15, 20, 25 are the first 5 natural numbers divisible by 5.

n=int(input())
for i in range(1,n+1):
      a=i*n
      print(a)