class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        columns = len(grid[0])
        islands = 0

        def bfs(i, j):
            queue = deque([(i, j)])
            grid[i][j] = '0'
            while len(queue) > 0:
                size = len(queue)
                for a in range(size):
                    m, n = queue.popleft()
                    for mx, ny in [(m+1, n), (m-1, n), (m, n+1), (m, n-1)]:
                        if 0 <= mx and mx< rows and 0 <= ny and ny< columns and grid[mx][ny] == '1':
                            grid[mx][ny] = '0'
                            queue.append((mx,ny))

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == '1':
                    bfs(i, j)
                    islands += 1

        return islands