"""
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""

"""
A start from all the gates and BFS level by level to reach the empty rooms. Even if we start from all the gates at the same time, 
the loop invariant is that we always finish finding all the nodes that are d-distance away before visiting the nodes that are 
(d+1)-distance away.

Time: O(mn), Space: O(mn).
"""
from collections import deque
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        m, n = len(rooms), len(rooms[0])
        queue = deque([])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        def inBound(x, y):
            return 0 <= x < m and 0 <= y < n
        
        # We always visit all the nodes that are d-distance away before visiting nodes that are (d+1)-distance away
        while queue:
            x, y = queue.popleft()
            dx = [1, 0, -1, 0]
            dy = [0, 1, 0, -1]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # We have visited this node before (or it's a wall), continue
                if not inBound(nx, ny) or rooms[nx][ny] != 2147483647:
                    continue
                rooms[nx][ny] = rooms[x][y] + 1
                queue.append((nx, ny))
