height = [1,8,6,2,5,4,8,3,7]

def maxArea(height):
    best = 0
    left = 0
    right = len(height) - 1

    while left < right:
        area = min(height[left], height[right]) * abs(left - right)
        if best < area:
            best = area
        if height[left] < height[right]:
            left += 1
        else: 
            right -= 1
    
    return best

print(maxArea(height)) 