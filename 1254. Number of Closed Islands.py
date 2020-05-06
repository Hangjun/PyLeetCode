"""
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:



Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:



Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
 

Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
"""

# Solution #1: Two Pass DFS. First identify the boundary islands, then count the closed islands. Time: O(mn), Space: O(mn).
class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        visited = [[False for i in range(n)] for j in range(m)]
        # find all islands connected to the boundary and mark them as visited to exclude them from counting
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m-1 or j == n-1) and grid[i][j] == 0:
                    self.dfs(grid, i, j, visited)
            
        count = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 0:
                    self.dfs(grid, i, j, visited)
                    count += 1
        
        return count
    
    
    def dfs(self, grid, x, y, visited):
        visited[x][y] = True
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not self.inBound(grid, nx, ny) or grid[nx][ny] or visited[nx][ny]:
                continue
            self.dfs(grid, nx, ny, visited)
            
    
    def inBound(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])
        
# Solution #2: One pass DFS. Handle the bondary check within the DFS by using a siimple flag. Time: O(mn), Space: O(mn).
class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        visited = [[False for i in range(n)] for j in range(m)]
            
        count = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 0:
                    self.flag = True
                    self.dfs(grid, i, j, visited)
                    if self.flag:
                        count += 1
        
        return count
    
    def dfs(self, grid, x, y, visited):
        if x == 0 or y == 0 or x == len(grid)-1 or y == len(grid[0])-1:
            self.flag = False
        visited[x][y] = True
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not self.inBound(grid, nx, ny) or grid[nx][ny] or visited[nx][ny]:
                continue
            self.dfs(grid, nx, ny, visited)
            
    
    def inBound(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])
