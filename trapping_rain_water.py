height = [0,1,0,2,1,0,1,3,2,1,2,1]

def trap(height):
        if not height:
            return 0
        
        l = 0
        r = len(height) - 1

        leftMax = height[l]
        rightMax = height[r]
        area = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                area += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                area += rightMax - height[r]
            
        return area

print(trap(height))