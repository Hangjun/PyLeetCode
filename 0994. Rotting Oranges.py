"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
"""

# BFS. Time: O(mn), Space: O(mn). Be careful with the corner case where there is no fresh oranges to begin with.
from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        freshCount = 0
        queue = deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    freshCount += 1
        
        # corner case: no fresh oranges to begin with
        if not freshCount:
            return 0
        
        time = 0
        
        # loop invariant: the oranges in the queue are rotten, but their neighbors might not
        while queue:
            if not freshCount:
                return time
            # scan level by level
            curSize = len(queue)
            for _ in range(curSize):
                x, y = queue.popleft()
                dx = [1, 0, -1, 0]
                dy = [0, 1, 0, -1]
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        freshCount -= 1
                    # otherwise it is either out of bound, or already rotten (hence existed in the queue),
                    # or is empty
            # current level is complete, increment the time count
            time += 1
        
        # cannot reach all the fresh oranges
        return -1
