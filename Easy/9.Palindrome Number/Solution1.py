x = 1211

import math

#Check if value is Negative
if(x<0):
    print(False)

# convert x into a array of intergers O(n)
num = []
while (x > 0):
    print(x)
    num.append(x%10)
    x = math.floor(x/10)
    
print(num) # check if array is complete

#find palinedrome by comparing last and first values O(n)
for i in range(math.ceil(len(num)/2)):
    lastIndex = (len(num)-1)-i #find the last index - i
    if(num[i] != num[lastIndex]):
        print("False")
        
print("True")