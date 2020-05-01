"""
In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

 

Example 1:

Input: [[0,1],[1,0]]
Output: 1
Example 2:

Input: [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Note:

1 <= A.length = A[0].length <= 100
A[i][j] == 0 or A[i][j] == 1
"""

"""
This is a great problem in which we get to apply both DFS and BFS. The BFS part is more or less intuitive: we start from the 
boundary of one island and expand level by level via BFS until we reach the second island. The DFS part is really to help us 
distinguish the two islands during the BFS expansion by first coloring one of the islands to a different color, much like we 
did in problem 827. 

We don't have to do this for this problem, but during the BFS, we color each newly reachable level by an increasing color. This 
can help us retrieve the actual bridge via backtracking if needed.

Time: O(mn), Space: O(mn).
"""
from collections import deque
class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        if not A or not A[0]:
            return 0
        m, n = len(A), len(A[0])
        color = 2
        queue = deque([])
        marked = False
        
        # Step #1: Color one of the island to 2 and place all the nodes into a queue
        for i in range(m):
            if marked: break
            for j in range(n):
                if A[i][j] == 1:
                    self.dfs(A, i, j, color, queue)
                    marked = True
                    break
                    
        # Step 2: Expand the colored island along the boundaries via BFS until we hit the second island
        while queue:
            curSize = len(queue)
            for _ in range(curSize):
                (x, y, dist) = queue.popleft()
                dx = [1, 0, -1, 0]
                dy = [0, 1, 0, -1]
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if not self.inBound(A, nx, ny):
                        continue
                    elif A[nx][ny] == 1: # found the second island
                        return dist
                    elif A[nx][ny] == 0: # found a 0 node, color it with color+1
                        A[nx][ny] = color+1
                        queue.append((nx, ny, dist+1))
                    else: # A[nx][ny] == color, it is a island node in the current level
                        continue
            color += 1
        return color

    def dfs(self, A, x, y, color, queue):
        A[x][y] = color
        queue.append((x, y, 0))
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if self.inBound(A, nx, ny) and A[nx][ny] == 1:
                self.dfs(A, nx, ny, color, queue)

    def inBound(self, A, x, y):
        return 0 <= x < len(A) and 0 <= y < len(A[0])
