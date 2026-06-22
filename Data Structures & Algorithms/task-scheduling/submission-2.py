class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        pq = []
        for key, val in freq.items():
            heapq.heappush_max(pq, val)

        cooldown = collections.deque()
        time = 0
        while pq or cooldown:
            time += 1
            if pq:
                remaining = heapq.heappop_max(pq) - 1
                if remaining > 0:
                    cooldown.append((remaining, time + n))

            if cooldown and cooldown[0][1] == time:
                count, _ = cooldown.popleft()
                heapq.heappush_max(pq, count)

        return time
