class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        n = len(grid)
        m = len(grid[0])
        def dfs(i, j):
            if (i, j) in visited: return
            visited.add((i,j))
            directions = [[1,0],[-1, 0],[0,1],[0,-1]]
            for x, y in directions:
                nx = i + x
                ny = j + y
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == "1" and (nx, ny) not in visited:
                    dfs(nx, ny)
        islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i, j)
                    islands +=1
        return islands
