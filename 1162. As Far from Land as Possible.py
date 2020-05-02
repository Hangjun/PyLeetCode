"""
Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

If no land or water exists in the grid, return -1.

 

Example 1:



Input: [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: 
The cell (1, 1) is as far as possible from all the land with distance 2.
Example 2:



Input: [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: 
The cell (2, 2) is as far as possible from all the land with distance 4.
 

Note:

1 <= grid.length == grid[0].length <= 100
grid[i][j] is 0 or 1
"""

# This is the exact same problem as Problem 994	Rotting Oranges. We start BFS from ALL the island cells at the same time and 
# cover the water cells level by level until the last water cell to get covered.
# Time: O(mn), Space: O(mn).
from collections import deque
class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        islandCount = waterCount = 0
        queue = deque([])
        visited = [[False for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    islandCount += 1
                    queue.append((i, j))
                    visited[i][j] = True
                else:
                    waterCount += 1
                    
        if not islandCount or not waterCount:
            return -1
        
        # BFS from all the islands at once and cover the water cell level by level
        dist = 0
        while queue:
            if not waterCount:
                return dist
            curSize = len(queue)
            for _ in range(curSize):
                x, y = queue.popleft()
                dx = [1, 0, -1, 0]
                dy = [0, 1, 0, -1]
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if not self.inBound(grid, nx, ny) or visited[nx][ny] or grid[nx][ny]:
                        continue
                    # (nx, ny) is a unvisited inbound water cell
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    waterCount -= 1
            dist += 1
        return -1
                    
    def inBound(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])
