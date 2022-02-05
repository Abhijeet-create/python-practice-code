# Red or Green
# Given a string, made up of only uppercase characters 'R' and 'G', where 'R' stands for Red and 'G' stands for Green. Find out the minimum number of characters you need to change to make the whole string of the same colour.

# Input
# One String.

# Output
# One Integer, denoting the minimum number of characters you need to change to make the whole string of the same colour.

# Example
# Input1:

# RGRGR
# Output1:

# 2
# Explanation:

# We need to change only the 2nd and 4th(1-index based) characters to 'R', so that the whole string becomes the same colour.

list=input()
count=0
sum=0
for i in range(len(list)):
 if list[i]=="G":
  count+=1
 else:
  sum+=1
if count<sum:
 print(count)
else:
 print(sum)
 
    