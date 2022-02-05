n=int(input())
if (n!=1):
  num=[]
  while n>0:
   num.append(int(input()))
   n=n-1
  for i in range(0,(len(num)-1)):
      sum=num[i]+num[i+1]
      if (sum>100):
         print("True")
         break
  if sum <= 100:
     print("False")