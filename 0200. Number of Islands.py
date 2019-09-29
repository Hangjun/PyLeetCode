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
import Queue as queue

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
        q = queue.Queue()
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    q.put((i, j))
                    visited[i][j] = True
                    # BFS on the neighbors of (i, j)
                    while q:
                        (x, y) = q.get()
                        dx = [-1, 0, 1, 0]
                        dy = [0, 1, 0, -1]
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if not self.inBound(grid, nx, ny) or visited[nx][ny] or grid[nx][ny] != '1':
                                continue
                            q.put((nx, ny))
                            visited[nx][ny] = True
                    res += 1
        return res
                        
    def inBound(self, grid, x, y):
        return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])

# Union-Find Solution.

# If we can modify the input, we can re-write the DFS solution by "sinking" the islands:
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0' # sink that node down
                # recursively sink the neighrboing connected nodes with '1'
                map(sink, (i-1, i, i+1, i), (j, j+1, j, j-1))
                return 1
            return 0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))
