class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        lo = 0
        hi = len(heights)-1

        while lo < hi:
            cur = (hi-lo) * min(heights[lo], heights[hi])
            max_water = max(cur, max_water)
            if heights[lo] < heights[hi]:
                lo +=1
            else:
                hi -= 1
        
        return max_water




