"""
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

 

Example 1:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: 12

Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
             The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: -1

Explanation: There is no way for the ball to stop at the destination.

 

Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
"""

"""
This problem is the extension of Problem 490 The Maze. Now we need to find the shortest path from start to destination. We can 
still use the DFS/BFS approach we took in Problem 490. The change is that, now we need to keep track of an auxiliary data structure 
dist[i][j] that records the shortest distance from start to (i, j), for each (i, j) in the maze. We can use either DFS or BFS to 
traverse ALL possible paths from start to destination while updating dist whenever we can. When we are done exhausting all the 
paths, we can then return dist[destination[0]][destination[1]].

Solution #1: DFS. 
Time: O(mn*max(m, n)) since for each node, we might need to take max(m, n) steps to reach a ball-stopping point.
Space: O(mn).
"""
# Actually get TLE on LeetCode.
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        if not maze or not maze[0]:
            return -1
        m, n = len(maze), len(maze[0])
        dist = [[sys.maxint for i in range(n)] for j in range(m)]
        dist[start[0]][start[1]] = 0
        self.dfs(maze, start, destination, dist)
        return dist[destination[0]][destination[1]] if dist[destination[0]][destination[1]] != sys.maxint else -1
    
    # traverse all possible paths to reach destination while recording the distances traveled
    def dfs(self, maze, start, destination, dist):
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            count = 0
            nx = start[0]
            ny = start[1]
            while self.inBound(maze, nx+dx[i], ny+dy[i]) and maze[nx+dx[i]][ny+dy[i]] == 0:
                nx += dx[i]
                ny += dy[i]
                count += 1
            # now (nx, ny) is a stop-ball location
            if dist[start[0]][start[1]] + count < dist[nx][ny]:
                dist[nx][ny] = dist[start[0]][start[1]] + count
                self.dfs(maze, [nx, ny], destination, dist)
                
    def inBound(self, maze, x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0])

# Solution #2: BFS. Accepted.
# Time: O(mn*max(m, n)), Space: O(mn).
from collections import deque
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        if not maze or not maze[0]:
            return -1
        m, n = len(maze), len(maze[0])
        dist = [[sys.maxint for i in range(n)] for j in range(m)]
        dist[start[0]][start[1]] = 0
        queue = deque([start])
        while queue:
            curNode = queue.popleft()
            dx = [1, 0, -1, 0]
            dy = [0, 1, 0, -1]
            for i in range(4):
                count = 0 # reset the count at the beginning of each new direction
                nx = curNode[0]
                ny = curNode[1]
                while self.inBound(maze, nx+dx[i], ny+dy[i]) and maze[nx+dx[i]][ny+dy[i]] == 0:
                    nx += dx[i]
                    ny += dy[i]
                    count += 1
                # We reached a ball-stopping point (nx, ny)
                if dist[curNode[0]][curNode[1]] + count < dist[nx][ny]:
                    dist[nx][ny] = dist[curNode[0]][curNode[1]] + count
                    queue.append([nx, ny])
        
        return dist[destination[0]][destination[1]] if dist[destination[0]][destination[1]] != sys.maxint else -1
                
    def inBound(self, maze, x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0])

# Remark: Notice that in the above DFS/BFS, we did not need to use a visited array. The reason is, if we have visited a given 
# node in the past, either it belongs to the same DFS/BFS search in which case it must have a strictly smaller distance, or it
# was visited at an earlier search path. In the second case, if we can update the distance to decrease it, then we need to visit 
# this node from the current path and re-DFS/BFS from that node. Otherwise we don't need to visit that node again. 

# Solution #3: Dijkstra Algorithm
"""
The inefficiency of DFS/BFS is that, some times we need to visit the same node multiple times, whenever we discover that we can 
decrease the distance of a node from the current search path. If we can make sure that once we have reached a node the 
distance is optimal and no revisit is needed, then we can reduce the running time. That's exactly the Dijkstra's Algorithm.

The methodology remains the same as the DFS or BFS Approach discussed above, except the order in which the current positions 
are chosen. We again make use of a distancedistance array to keep a track of the minimum number of steps needed to reach every 
position from the startstart position. At every step, we choose a position which hasn't been marked as visited and which is 
at the shortest distance from the startstart position to be the current position. We mark this position as visited so that we 
don't consider this position as the current position again.

# Time: O(mn*log(mn)), Space: O(mn).
"""
from heapq import heappush, heappop, heapify
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        if not maze or not maze[0]:
            return -1
        m, n = len(maze), len(maze[0])
        dist = [[sys.maxint for i in range(n)] for j in range(m)]
        dist[start[0]][start[1]] = 0
        pq = []
        heappush(pq, (0, start))
        while pq:
            distance, curNode = heappop(pq)
            # we can exit early as soon as we reach the destination
            if curNode == destination:
                return distance
            dx = [1, 0, -1, 0]
            dy = [0, 1, 0, -1]
            for i in range(4):
                count = 0 # reset the count at the beginning of each new direction
                nx = curNode[0]
                ny = curNode[1]
                while self.inBound(maze, nx+dx[i], ny+dy[i]) and maze[nx+dx[i]][ny+dy[i]] == 0:
                    nx += dx[i]
                    ny += dy[i]
                    count += 1
                # We reached a ball-stopping point (nx, ny)
                if dist[curNode[0]][curNode[1]] + count < dist[nx][ny]:
                    dist[nx][ny] = dist[curNode[0]][curNode[1]] + count
                    heappush(pq, (dist[nx][ny], [nx, ny]))
        
        return dist[destination[0]][destination[1]] if dist[destination[0]][destination[1]] != sys.maxint else -1
                
    def inBound(self, maze, x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0])





