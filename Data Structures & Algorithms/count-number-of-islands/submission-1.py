class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        columns = len(grid[0])
        islands = 0

        def dfs(i, j):
            grid[i][j] = '0'
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < rows and 0 <= y < columns and grid[x][y] == '1':
                    grid[x][y] = '0'
                    dfs(x,y)

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == '1':
                    dfs(i, j)
                    islands += 1

        return islands