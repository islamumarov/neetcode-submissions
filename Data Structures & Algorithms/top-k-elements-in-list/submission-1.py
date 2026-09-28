class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        pq = []
        for key, freq in counter.items():
            heapq.heappush(pq, (-freq, key))

       # print(pq)

        return [heapq.heappop(pq)[1] for _ in range(k)]
        
        

