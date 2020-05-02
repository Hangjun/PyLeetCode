"""
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7 

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total 
             travel distance of 3+3+1=7 is minimal. So return 7.
Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
"""

"""
This is a typical BFS problem. We can either start the BFS from each empty land to calculate the minimum distance to reach all 
the buildings, or start the BFS from each building and calculate the minimum distance to reach all the empty land. The time 
complexity depends on the number of buildings and the number of empty land. More specifically, let the grid of size m x n with 
B buildings and E empty land. If we start from the land, it takes O(Emn) time and O(mn) space. If we start from the buildings it 
takes O(Bmn) time and O(mn) space. We solve this problem by taking the latter approach: start the BFS from each building and 
incrementally update the distance from each building to each empty land.

BFS. Time: O(m^2n^2), Space: O(mn).
"""
from collections import deque
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: 
            return 0
        m, n = len(grid), len(grid[0])
        buildingCount = 0        
        # total distance from (i, j) to all buildings reachable
        dist = [[0 for i in range(n)] for j in range(m)]
        # total number of reachable buildings from (i, j)
        reachable = [[0 for i in range(n)] for j in range(m)]
        
        # Step 1: for each building, BFS to update all the distance from this building to an empty land
        # Time: O(m^2n^2)
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1: 
                    continue
                buildingCount += 1
                visited = [[False for _ in range(n)] for _ in range(m)]
                queue = deque([(i, j)])
                visited[i][j] = True
                level = 1
                # BFS to update the shortest distance from this building to all reachable empty land
                while queue:
                    curSize = len(queue)
                    for _ in range(curSize):
                        x, y = queue.popleft()
                        dx = [1, 0, -1, 0]
                        dy = [0, 1, 0, -1]
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if not self.inBound(grid, nx, ny) or visited[nx][ny] or grid[nx][ny]: 
                                continue
                            dist[nx][ny] += level
                            reachable[nx][ny] += 1
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                            #print('update distance for {}, {} to be {}, reachable buildings = {}'.format(nx, ny, dist[nx][ny], reachable[nx][ny]))
                    level += 1
        
        # Step 2: find the land with minimum total distance to all buildings. Time: O(mn).
        res = sys.maxint
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reachable[i][j] == buildingCount:
                    res = min(res, dist[i][j])
        return res if res != sys.maxint else -1
            
    def inBound(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])
