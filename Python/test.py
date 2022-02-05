# test casse:
# 1. m is negetive and n is positive.
# [-35,-20]
# ouput will be -1

# 2.both m and n are negetive.
# [1,50]
# starts form 1   goes upto 50 one element per line

# 3.both m and n are positive.

# [-15,30]

# start from zero goes upto 30.

# steps to do:
# 1. input the first element of range
# 2.input the second element of range.
# 3.if m<0 and n<0;
#     then print -1
# 4.else
#     run for loop from m to n and check the condition if i>=0 then print i.


m=int(input())
n=int(input())
if m<0 and n<0:
 print(-1)
else:
 for i in range (m,n+1):
   if i>=0:
    print(i)
