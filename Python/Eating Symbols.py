#Eating Symbols
#There is always an integer in Rakesh's mind.

#Initially, the integer in Rakesh's mind is 0. Rakesh is now going to eat four symbols, each of which is + or -. When he eats +, the integer in his mind increases by 1; when he eats -, the integer in his mind decreases by 1.

#The symbols Rakesh is going to eat are given to you as a string S. The i-th character in S is the i-th symbol for him to eat.

#Find the integer in Rakesh's mind after he eats all the symbols.

#Input
#One String, denoting S.

#Output
#One Integer, denoting the result.

#Example
#Input1:

#+-++
#Output1:

#2
#Explanation1:

#Initially, the integer in Rakesh's mind is 0.
#The first integer for him to eat is +. After eating it, the integer in his mind becomes 1.
#The second integer to eat is -. After eating it, the integer in his mind becomes 0.
#The third integer to eat is +. After eating it, the integer in his mind becomes 1.
#The fourth integer to eat is +. After eating it, the integer in his mind becomes 2.

#Thus, the integer in Rakesh's mind after he eats all the symbols is 2.

s=input()
list=s.split()
num=0
for i in range(len(s)):
   if s[i]=="+":
     num=num+1
   else:
     num=num-1
print(int(num))