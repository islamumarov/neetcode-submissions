class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsMap = set()
        for i in nums:
            numsMap.add(i)
        maxConsecs = 0
        for j in nums:
            consecs = 0
            i = j
            while j + 1 in numsMap:
                consecs += 1
                numsMap.remove(j+1)
                j += 1
            while i - 1 in numsMap:
                consecs += 1
                numsMap.remove(i - 1)
                i -= 1
            maxConsecs = max(maxConsecs, consecs+1)

        return maxConsecs
