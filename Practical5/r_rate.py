n = 84
r = 1.1
for i in range (1,6):
    new = r * n
    total = new + n
    n = total

import math
total = math.floor(total)
print('The total number of individuals infected after 5 generations is', total, 'if the r rate is', r)


# Check for r = 1.1 (should be 3430 infections)

# new is newly infected people
# b is infected people in last round
# c is the total ifected people after this round
# five rounds of infection
