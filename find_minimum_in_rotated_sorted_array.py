import math

nums = [3,4,5,1,2]
nums=[2,1]

def findMin(nums):
    l = 0
    r = len(nums) - 1
    curr_min = nums[0]
    while l <= r:
        if nums[l] < nums[r]:
            res = min(curr_min, nums[l])
            break
        
        mid = (l + r) // 2 
        if nums[mid] < curr_min:
            curr_min = nums[mid]
        
        if nums[mid] >= nums[l]:
            l = mid + 1
        else:
            r = mid - 1
    
    return curr_min

print(findMin(nums))