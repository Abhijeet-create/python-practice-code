

n=int(input())
arr=[]
for i in range(n):
  arr.append(int(input()))
count=1
for i in range(n-1):
  if arr[i]==arr[i+1]:
    count+=1
  if arr[i]!=arr[i+1]:
    if count==arr[i]:
     break 
    count=1
if count==1 and arr[0]!=1:
  print(-1)
else:
 print(count)


# 1 2 2 3 3 3

