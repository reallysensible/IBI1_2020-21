a=190502
b=190784
c=100320
d=abs(a-c)
e=abs(a-b)
if d > e:
    print ("d is greater")
elif d < e:
    print ("e is greater")
else:
    print ("d is equal to e")
X = 1>1
Y = 1<2
Z = (X and not Y) or (Y and not X)
W = X!=Y
print(W == Z)
