"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""

# DFS Solution. Time: O(mn), Space: O(mn)
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for i in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != '1' or visited[i][j]:
                    continue
                self.dfs(grid, i, j, visited)
                res += 1
        return res
    
    def dfs(self, grid, x, y, visited):
        visited[x][y] = True
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if self.inBound(grid, nx, ny) and not visited[nx][ny] and grid[nx][ny] == '1':
                self.dfs(grid, nx, ny, visited)
                
    def inBound(self, grid, x, y):
        return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])

# BFS Solution. Time: O(mn), Space: O(mn)

# Union-Find Solution.

# Very sick Python solution: Sink the island.
