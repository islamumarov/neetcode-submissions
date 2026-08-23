class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for i, j in enumerate(stones):
            heapq.heappush(pq, -j)
        
        while len(pq) > 1:
            first, second = heapq.heappop(pq), heapq.heappop(pq)
            if first == second:
                continue
            else:
                heapq.heappush(pq, -abs(first-second))
        
        return -pq[0] if len(pq) > 0 else 0
