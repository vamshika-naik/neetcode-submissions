class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        columns = len(grid[0])
        max_area = 0

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= columns or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            area = 1
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < rows and 0 <= y < columns and grid[x][y] == 1:
                    area += dfs(x, y)
            return area   

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    max_area = max(area, max_area)

        return max_area