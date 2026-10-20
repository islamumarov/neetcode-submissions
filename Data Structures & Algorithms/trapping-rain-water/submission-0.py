class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0
        rightMax = [0] * len(height)
        rightMax[-1] = height[-1]
        for i in range(len(height)-2,-1,-1):
            rightMax[i] = max(height[i], rightMax[i+1])
        
        leftMax = 0
        for i in range(len(height)):
            leftMax = max(leftMax, height[i])
            water += min(leftMax, rightMax[i]) - height[i]
        
        return water

