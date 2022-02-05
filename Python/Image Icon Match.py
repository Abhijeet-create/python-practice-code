# Image Icon Match
# You are given a 1D image. The image is a sequence of pixel values. You are also given an icon of a particular size. The icon is a sequence of 2 pixels. Find the number of times this icon appears in the image.

# Input
# First line contains n, the number of pixels in the image. This is followed by n lines, each containing one positive integer denoting a pixel, j, 0 <= j <= 255. This is followed by m, the number of pixels in the icon. This is follwoed by m lines, each containing one positive interger denoting a pixel k, 0 <= k <= 255.

# Output
# An integer i i >= 0, denoting the number of times the icon appears in the image.

# Example
# Input:

# 10
# 7
# 27
# 31
# 8
# 9
# 10
# 25
# 8
# 9
# 11
# 2
# 8
# 9
# Output:

# 2
# The first line is 10 i.e. 10 pixels in the given image 7, 27, 31, 8, 9, 10, 25, 8, 9, 11 is the given image After this, the line contains 2, i.e. 2 pixels in the icon 8, 9 is the given icon. 8, 9 appears twice in the image. So 2 is the answer.

n= int(input())
l=[]
for i in range(n):
 l.append(int(input()))
m=int(input())
l2=[]
for i in range(m):
 l2.append(int(input()))
if m==0:
 print(0)
elif m==1:
 count=0
 for i in range(n):
  if l2[0]==l[i]:
   count+=1
 print(count)
else:
 count=0
 for i in range(1,n):
  if l2[1]==l[i] and l2[0]==l[i-1]:
   count+=1
 print(count)



  