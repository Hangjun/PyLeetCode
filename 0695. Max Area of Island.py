"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""

# Solution #1: DFS with book keeping. Time: O(mn), Space: (mn). Assuming that we cannot modify the input. 
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for i in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1 or visited[i][j]:
                    continue
                res = max(res, self.dfs(grid, i, j, visited) + 1)
        return res
    
    def dfs(self, grid, x, y, visited):
        res = 0
        visited[x][y] = True
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not self.inBound(grid, nx, ny) or visited[nx][ny] or grid[nx][ny] != 1:
                continue
            res += 1 + self.dfs(grid, nx, ny, visited)
        return res
    
    def inBound(self, grid, x, y):
        return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])

# A different implementation of the above:
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for i in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and not visited[i][j]:
                    res = max(res, self.dfs(grid, i, j, visited))
        return res
    
    def dfs(self, grid, x, y, visited):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and not visited[x][y] and grid[x][y]:
            visited[x][y] = True
            return 1 + self.dfs(grid, x-1, y, visited) + self.dfs(grid, x, y+1, visited) + self.dfs(grid, x+1, y, visited) + self.dfs(grid, x, y-1, visited)
        else:
            return 0

# Solution #2: DFS with book keeping. Time: O(mn), Space: O(1). Assuming that we can modify the input.
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = 0
                return 1 + sink(i-1, j) + sink(i, j+1) + sink(i+1, j) + sink(i, j-1)
            else:
                return 0
        return max(sink(i, j) for i in range(m) for j in range(n))
