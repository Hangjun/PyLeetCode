"""
In a 2D grid of 0s and 1s, we change at most one 0 to a 1.

After, what is the size of the largest island? (An island is a 4-directionally connected group of 1s).

Example 1:

Input: [[1, 0], [0, 1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: [[1, 1], [1, 0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: [[1, 1], [1, 1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
 

Notes:

1 <= grid.length = grid[0].length <= 50.
0 <= grid[i][j] <= 1.
"""

# DFS. Time: O(mn), Space: O(mn).
class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        visited = [[False for i in range(n)] for j in range(m)]
        index = 2 # to disinguish from 0 and 1
        areaMap = {} # index -> area of the island
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    areaMap[index] = self.dfs(grid, i, j, index)
                    index += 1
        if not areaMap:
            return 1
        res = max(areaMap.values())
        print(grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    possibleIslands = set()
                    dx = [1, 0, -1, 0]
                    dy = [0, 1, 0, -1]
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if not self.inBound(grid, nx, ny) or grid[nx][ny] < 2:
                            continue
                        possibleIslands.add(grid[nx][ny])
                    res = max(res, sum(areaMap[ind] for ind in possibleIslands) + 1)
        
        return res
    
    def dfs(self, grid, x, y, index):
        curArea = 1
        grid[x][y] = index
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if self.inBound(grid, nx, ny) and grid[nx][ny] == 1:
                curArea += self.dfs(grid, nx, ny, index)
        return curArea
    
    def inBound(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])
