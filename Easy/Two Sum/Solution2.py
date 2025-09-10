nums = [2, 7, 11, 15]
target = 9

#Big(O) = N
seen = {}
for i, n in enumerate(nums): #loop through nums with index
    remainer = target - n # find the opposite value
    if remainer in seen: # check if the opposite value is in seen dictionary
        print([seen[remainer],i]) # if found output 
    seen[n] = i # add the value in dictionary marked as already found