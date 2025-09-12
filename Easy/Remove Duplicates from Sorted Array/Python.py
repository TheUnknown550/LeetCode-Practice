from typing import List

def removeDuplicates(nums: List[int]) -> int:
    if not nums:
        return 0

    # pointer for the position of last unique element
    i = 0

    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]  # overwrite in-place
            
    print(nums)

    return i + 1  # new length

def main():
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(removeDuplicates(nums))
    
if __name__ == "__main__":
    main()
    
