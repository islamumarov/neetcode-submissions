class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        leftMax, rightMax = 0, 0
        water = 0
        while l < r:
            rightMax, leftMax=max(height[r], rightMax), max(leftMax, height[l])

            
            if rightMax < leftMax:
                water += min(rightMax, leftMax) - height[r]
                r -=1
            else:
                water += min(rightMax, leftMax) - height[l]
                l +=1
        
        return water

