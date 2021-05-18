n = 84
r = 1.1

# Repeat for five times:
#   newly infected people = r * total infected people in last round
#   total infected people this round = newly infected people + total infected people in last round
#   done
for i in range (1,6):
    new = r * n # total infected people in last round
    n = new + n # now n becomes the total infected people this round

# approximate the result (I ignore the decimals as numbers of people only can be integers.)
import math
n = math.floor(n)
print('The total number of individuals infected after 5 generations is', n, 'if the r rate is', r)
