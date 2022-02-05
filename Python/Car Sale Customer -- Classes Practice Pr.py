# Car Sale Customer -- Classes Practice Problems
# You are moving to a different country and you want to sell your car. You bought your car for 10,00,000 Rs (10 Lakhs). You are not willing to sell the car if the customers offer you less than 90% of what you paid. You have customers lined up offering you what they are willing to pay and you have to come up with the list of customers who you can sell your car to. Each customer will submit one proposal.
# Design a class CarSell which has 1 method.
# getCustomerInput -- This method should get the indices of all the customers whose proposals are greater than or equal to 90% of the car value.
# If all the customers are only willing to pay less than 90%, print -1

# Input
# First line contains n, an integer denoting the number of customers 0<n<=100.
# Next n lines will contain n integer one for each of the proposals received from n customers.

# Output
# m denoting the index of the prospective customers whose proposals are greater than or equal to 90% of car value.

# Example
# Input:

# 3
# 1000000
# 100000
# 900000
# Output:

# 0
# 2
# First line is 3, i.e. 3 test cases.
# Second line contains customer at 0th index whose proposal is 10Lakhs.
# Third line contains customer at index 1 whose proposal is 1Lakh.
# Fourth line contains customer at index 2 whose proposal is 9Lakhs.
# As the proposals of 0th and 2nd customer are the only ones greater than or equal to 90% of the car value. We print the output as 0 and 2

class CarSell():
 def __init__(self,l):
  self.value=(0.9*1000000)
  self.customer_list=l

 def getCustomerInput(self):
   c=0
   for i in range(len(self.customer_list)):
    if self.customer_list[i]>=self.value:
     print(i)
     c+=1
   else:
     if c==0:
      print(-1)
         
n=int(input())
l=[]
for i in range(n):
 l.append(int(input()))
l1=CarSell(l)
l1.getCustomerInput()