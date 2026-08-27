class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        max_area = 0
        visited = set()
        def dfs(i, j) -> int:
            if (i,j) in visited:
                return 0
            visited.add((i, j))
            directions = [[1,0],[-1, 0],[0, 1],[0,-1]]
            

            area = 1
            for x, y in directions:
                nx = i + x
                ny = j + y
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and (nx, ny) not in visited:
                    area += dfs(nx, ny)
            return area
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i, j) not in visited:
                    cur_area = dfs(i,j)
                    max_area = max(max_area, cur_area)
        
        return max_area






