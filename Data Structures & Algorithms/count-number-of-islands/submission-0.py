class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or 
                c >= COLS or grid[r][c] == "0"
            ):
                return

            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Go to every grid number
        for r in range(ROWS):
            for c in range(COLS):
                # If number == '1', start DFS
                if grid[r][c] == "1":
                    # For every node visited, turn it into "0"
                    dfs(r, c)
                    # Keep count of how many DFS we ran
                    islands += 1

        return islands
