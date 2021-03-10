# initial infected individual n
n=84
i=0
# r rate
r=1.2
# a is newly infected people
# b is infected people in last round
# c is the total ifected people after this round
b=n
c=n
# five rounds of infection
while i<5:
 a=r*b #a=1.2*84 1.2*
 c=a+c #c=1.2*84+84
 b=a
 i=i+1

print (c)
