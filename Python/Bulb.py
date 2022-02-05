# Bulb
# There is a bulb. Just like other bulbs, this bulb can be either ON or OFF at a time. You can provide 3 types of instruction to the bulb-

# "ON"-> turn the bulb on.(no matter the previous state)
# "OFF"-> turn the bulb off.(no matter the previous state)
# "Toggle"-> If the bulb was initially on, turn it off. If the bulb was initially off, turn it on.
# You provide the bulb with 'N' number of Queries, each containing either of the above 3 instructions. Count the number of times bulb was turned ON from a OFF position.(ON->OFF)

# Note- Intially assume that the bulb was OFF.

# Input
# First line of the input contains N, representing the number of instructions. The following N lines contain one of the 3 types of instructions "ON","OFF","Toggle".

# Output
# Finally print the number of times the bulb was turned ON from a OFF position.

# Example
# Input:

# 5

# Toggle

# Toggle

# OFF

# Toggle

# ON

# Output:

# 2

# Explanation:

# Intially : OFF

# | BEFORE | INSTRUCTION | RESULT |
# ------------------------------------
# | OFF        | TOGGLE           | ON |
# | ON          | TOGGLE           |OFF|
# | OFF        | OFF                  | OFF |
# | OFF        | TOGGLE           | ON |
# | ON          | ON                   | ON |
# As we can see that the bulb has been switched from OFF to ON 2 times once during the first(TOGGLE) instruction and then during the 4th(TOGGLE) instruction. So the output is 2


n=int(input())
state= "OFF"
count=0
for i in range(n):
 ins=input()
 if ins=="Toggle" and state=="OFF":
   count+=1
   state="ON"
 elif ins=="Toggle" and state=="ON":
   count=count
   state="OFF"
 elif ins=="ON" and state=="OFF":
    count+=1
    state="ON"
 elif ins=="ON" and state=="ON":
    count=count
 else:
     state="OFF"
print(count)
    
   
 