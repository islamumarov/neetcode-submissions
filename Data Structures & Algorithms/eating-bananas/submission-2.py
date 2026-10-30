class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        if len(piles) == h: return max(piles)
        lo, hi = 0, max(piles)
        def canEat(mid):

            return sum([piles[i]//mid + (1 if piles[i] % mid != 0 else 0) for i in range(len(piles))]) <= h

        while lo < hi:
            mid = (lo + hi) // 2
            if canEat(mid):
                hi = mid
            else:
                lo = mid+1
        
        return lo


