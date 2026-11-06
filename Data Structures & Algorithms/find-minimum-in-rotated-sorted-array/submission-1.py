class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_elem = 0

        for i in range(len(nums)):
            if nums[i] < nums[min_elem]:
                min_elem = i

        
        return min(min_elem, len(nums) - min_elem -1)
        