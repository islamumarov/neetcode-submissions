class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res: List[List[int]] = []
        #-4,-1,-1, 0, 1, 2
 #           |.  |.       |
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue
            j = i+1
            k = len(nums)-1
            while j < k:
                curSum = nums[i] + nums[j] + nums[k]
                if curSum > 0:
                    k -= 1
                elif curSum < 0:
                    j += 1
                else:
                    while j < len(nums)-1 and nums[j] == nums[j+1]: j+=1
                    while k > 0 and nums[k] == nums[k-1]: k-=1
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k -=1

        return res