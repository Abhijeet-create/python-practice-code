# min max range
# Given 3 lists of positive integers. From the first list get the minimum value m1 and second list get the maximum value m2. From the third list get all the values that lies between m1 and m2 including m1 and m2.

# If m1 <= m2 then we should consider all the values x from third list which stisifies m1 <= x <= m2

# If m1 > m2 then we should consider all the values x from third list which stisifies m1 >= x >= m2

# You have write 3 functions.

# Takes list as input and returns a minimum value.
# Takes list as input and returns a maximum value.
# Takes a list, m1 and m2 and returns list of intergers which lies between m1 and m2. If no such numbers exist return a list with -1 i.e [-1]
# You have to return the list of numbers in the same order they are present.

# You will be provided with function template, you have to fill those functions.

# Input
# [3,5,4,5,7]

# [7,6,4,4,23,2]

# [6,5,1,3,8,9,2]

# Output
# [6,5,3,8,9]

def minimum_value(input_numbers):
 return min(input_numbers)

def maximum_value(input_numbers):
 return max(input_numbers)
 
def get_numbers_in_range(input_numbers,m1,m2):
 res=[]
 if m1<=m2:
  for i in range(len(input_numbers)):
  	if m1<=input_numbers[i]<=m2:
  	 res.append(input_numbers[i])
 else:
  for i in range(len(input_numbers)):
  	if m1>=input_numbers[i]>=m2:
  	 res.append(input_numbers[i])
 if len(res)==0:
  return [-1]
 else:
  return res

l1=[int(x) for x in input().split()]
l2=[int(x) for x in input().split()]
l3=[int(x) for x in input().split()]
m1=minimum_value(l1)
m2=maximum_value(l2)
print(get_numbers_in_range(input_numbers,m1,m2))