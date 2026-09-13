class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        queue = deque()

        for i in range(0, n):
            for j in range(0, m):
                if grid[i][j] == 0:
                    queue.append((i,j))
        

        dist = 0
        LAND = 2147483647

        while queue:
            dist +=1

            qLen = len(queue)
            for _ in range(qLen):
                i, j = queue.popleft()
                for ni, nj in [[1, 0],[-1, 0], [0, 1], [0, -1]]:
                    nx,ny = i + ni, j + nj
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == LAND:
                        grid[nx][ny] = dist
                        queue.append((nx, ny))
        







