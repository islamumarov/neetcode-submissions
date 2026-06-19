class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = []
        for i, j in freq.items():
            heapq.heappush_max(heap, j)

        cooldown = collections.deque()
        time = 0

        while heap or cooldown:
            time += 1
            if heap:
                remain = heapq.heappop_max(heap) - 1
                if remain > 0:
                    cooldown.append((remain, time + n))

            if cooldown and cooldown[0][1] == time:
                ready = cooldown.popleft()[0]
                heapq.heappush_max(heap, ready)

        return time

