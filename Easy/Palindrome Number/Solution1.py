x = 121

import math

num = []
while (x > 0):
    print(x)
    num.append(x%10)
    x = math.floor(x/10)
    
print(num)