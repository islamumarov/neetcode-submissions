class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0

        while i < len(nums):
            if nums[i] == i+1: i+=1
            else:
                if nums[i] == nums[nums[i-1]]:
                    return nums[i]

        return -1


