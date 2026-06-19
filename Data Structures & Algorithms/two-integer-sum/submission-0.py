class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        ns = {}
        for i,j in enumerate(nums):
            if target - j in ns:
                second = ns[target-j]
                res.append(second)
                res.append(i)
            ns[j] = i
        
        return res