class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productsOfNums = 1
        zeros = 0
        for i in nums:
            if i == 0:
                zeros +=1
                continue
            productsOfNums *= i
        if zeros > 1:
            return [0] * len(nums)
        if zeros == 1:
            return [int(productsOfNums) if item == 0 else 0 for item in nums]
        return [int(productsOfNums/item) if item != 0 else 0 for item in nums]



