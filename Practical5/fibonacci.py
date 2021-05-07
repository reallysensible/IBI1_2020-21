a=1     # a = the first value
b=1     # b = the second value
fibonacci=[1,1]     # known fibonacci = [1,1]
#a = (i-2)th, b = (i-1)th, c = ith
for i in range (3,14):      # Repeat for 11 times (calculate 3rd-13th values)
    c=a+b   # 3rd = 1st + 2nd (ith = (i-2)th + (i-1)th)
    a=b     # new 1st = 2nd (new (i-2)th = (i-1)th)
    b=c     # new 2nd = 3rd (new (i-1)th = ith)
    i=i+1
    fibonacci.append(c)     # record the newly calculated value in fibonacci

print(fibonacci)

# the 1st and 2nd values are known
# calculate the 3rd-13th values:
#   3rd = 1st + 2nd, i = 3
#   4th = 2nd + 3rd, i = 4
#   5th = 3rd + 4th, 1 = 5
#   ...... (ith = (i-2)th + (i-1)th, i = i + 1)
#   13th = 11th + 12th, i = 13
#   if i = 13: stop calculating
#   record all the values in fibonacci


#   ith = (i-2)th + (i-1)th
#   i = i+1 in the next cycle

# Repeat:
#   calculate
#   How many times calculated?
#       if less than 11 times: keep calculating
#       if 11 times: stop calculating
#   record the values in fibonacci
#   done
