# Max occurrences
# Given a sorted list of n non negative integers. Find the integer which is occurring the maximum number of times. If no such number exists, please print -1. If there are multiple numbers with the same maximum occurrence count. Print all of them in ascending order.

# Input
# First line n denoting the length of the list Following n lines contains the elements of the list

# Output
# m lines containing the numbers which are occurring the maximum number of times

# Example
# Input:

# 5
# 1
# 2
# 2
# 2
# 3
# Output:

# 2
# 5 denotes the length of the list. 1 is occurring once and so is 3. 2 is occurring 3 times which is the maximum. So 2 is the output

# Input:

# 5
# 1
# 2
# 2
# 3
# 3
# Output:

# 2
# 3
# 5 denotes the length of the list. 1 is occuring only once. 2 is occuring 2 times and 3 is also occuring 2 times which is the maximum times a number is occuring in the given list. So 2 and 3 both are in the output.


n=int(input())
l=[]
for i in range (n):
 m=int(input())
 l.append(m)
if len(l)==0:
 print(-1)
else:
 count=1
 maxx=1
 for i in range(len(l)-1):
   if l[i]==l[i+1]:
     count+=1
     maxx=max(maxx,count)
     continue
   count=1
 res=[-1]
 for i in l:
   if (l.count(i)==maxx and res[-1]!=i):
     res.append(i)
 for i in res:
   if i!=-1:
     print(i)


 



