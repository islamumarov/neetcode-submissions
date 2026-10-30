class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:      

        if len(piles) == h:
            return max(piles)

        lo, hi = min(piles)//h, max(piles)

        def canEat(mid):
            sums = 0 
            for i in range(len(piles)):
                sums += math.ceil(piles[i] / mid)
            
            return sums <= h


        while lo < hi:
            mid = (lo + hi) // 2
            if canEat(mid):
                hi = mid
            else:
                lo = mid+1
        
        return lo

# 1, 3, 9 s=5
# 
# T = O(N * log(max(array)))
# S = O (1)