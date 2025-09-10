nums = [2, 7, 11, 15]
target = 9

#Big(O) = N^2
for i in range(len(nums)):
    for j in range(i + 1, len(nums)): # loop through all values similar to traversal in a 2 dimentional array
        if nums[i] + nums[j] == target: # if found return it
            print([i, j])
            
    