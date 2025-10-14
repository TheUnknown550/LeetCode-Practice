from typing import List

def removeElement(nums, val):
    for i, n in enumerate(nums):
        if n == val:
            if i + 1 < len(nums) and nums[i+1] != n:
                nums[i] = nums[i+1]
                nums[i+1] = n
                print(nums[i], nums[i+1])
            else:
                nums[i] = 0
    return nums

def main():
    nums = [3,2,2,3,2]
    val = 3
    print(removeElement(nums, val))

if __name__ == "__main__":
    main()
    
