

def hasDuplicate(nums):
    seen = {}
    for char in nums:
        if char not in seen:
            seen[char] = True
        else:
            return False
    return True

