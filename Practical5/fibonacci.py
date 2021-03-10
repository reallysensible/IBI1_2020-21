a=1
b=1
#a: (i-2)th, b:(i-1)th, c:ith
for i in range (3,14):
 c=a+b
 a=b
 b=c
 print(i,c)
