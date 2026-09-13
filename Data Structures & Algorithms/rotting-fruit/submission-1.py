class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        q = deque()
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh +=1


        minutes = 0
        while q and fresh > 0:
            minutes +=1
            qLen = len(q)
            for _ in range(qLen): # (2, 2)
                i, j = q.popleft()
                for ni, nj in [[1,0],[-1,0], [0,-1], [0,1]]:
                    nx, ny = i + ni, j + nj #
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -=1
                        q.append((nx, ny))
        
        return minutes if fresh == 0 else -1





