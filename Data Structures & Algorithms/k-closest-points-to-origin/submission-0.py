class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        def euclid_dis(x, y):
            return math.sqrt(x**2 + y**2)
        for xi, yi in points:
            heapq.heappush(pq, (euclid_dis(xi, yi), [xi, yi]))
        res = []
        for _ in range(0, k):
            x,y = heapq.heappop(pq)[1]
            res.append([x,y])

        return res
    
    