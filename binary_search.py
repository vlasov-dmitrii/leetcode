
arr = [ 2, 3, 4, 10, 40 ]

def search(nums, target):
    low = 0
    high = len(nums) - 1
    mid = 0
    
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
        
        elif nums[mid] > target:
            high = mid - 1
        
        else: 
            return mid
    
    return -1

print(search(arr, 3))