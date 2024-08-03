nums = [0,0,1,1,1,2,2,3,3,4]

def removeDuplicates(nums):
    seen = {}
    for i in range(len(nums)):
        if nums[i] not in seen:
            seen[nums[i]] = 1
    j = 0
    unique = len(seen)
    for key in seen:
        nums[j] = key
        j += 1
    
    for i in range(len(nums)):
        if i < unique: 
            continue
        else:
            nums[i] = "_"
    
    return unique

print(removeDuplicates(nums))