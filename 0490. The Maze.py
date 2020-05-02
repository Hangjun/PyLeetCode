"""
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

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

Output: true

Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: false

Explanation: There is no way for the ball to stop at the destination.

 

Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
"""

"""
The tricky part is how to handle the rolling. To implement this rolling, when we find the neighbors [nx, ny], we cannot stop 
at one step away like before: nx = x + dx[i], ny = y + dy[i]. Instead, we need to check the inBound and grid value condition 
in a given direction (controlled by i) until we hit a wall. 

Another tricky part is the handling of visited in this case. It is wrong to return False as soon as we bump into a visited node.
We just need to go to the next candidate. Also notice that we do not mark intermediate nodes (the ones in the rolling) as visited.
Only the nodes where we stop at are marked as visited.
"""

# DFS. Time: O(mn), Space: O(mn).
class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        if not maze or not maze[0]:
            return False
        m, n = len(maze), len(maze[0])
        visited = [[False for i in range(n)] for j in range(m)]
        return self.dfs(maze, start, destination, visited)
    
    def dfs(self, maze, start, destination, visited):
        if start == destination:
            return True
        
        x, y = start[0], start[1]
        visited[x][y] = True
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            print('i = ', i)
            nx = x
            ny = y
            while self.inBound(maze, nx+dx[i], ny+dy[i]) and maze[nx+dx[i]][ny+dy[i]] == 0:
                nx += dx[i]
                ny += dy[i]
            if visited[nx][ny]:
                continue # CAUTION: if visited, we go to the next location instead of returning False!
            if self.dfs(maze, [nx, ny], destination, visited):
                return True
        
        return False
    
    def inBound(self, maze, x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0])

"""
We can also solve this problem using BFS. The neighbors of each node is now defined to be the nodes eminating from the current 
node which the ball can stop at. Then we continue the search onward from those nodes. The complexity is the same as DFS. From 
OJ, the time is slightly faster.

BFS: Time: O(mn), Space: O(mn).
"""
from collections import deque
class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        if not maze or not maze[0]:
            return False
        m, n = len(maze), len(maze[0])
        visited = [[False for i in range(n)] for j in range(m)]
        visited[start[0]][start[1]] = True
        queue = deque([start])
        while queue:
            curNode = queue.popleft()
            if curNode == destination:
                return True
            dx = [1, 0, -1, 0]
            dy = [0, 1, 0, -1]
            for i in range(4):
                nx = curNode[0]
                ny = curNode[1]
                while self.inBound(maze, nx+dx[i], ny+dy[i]) and maze[nx+dx[i]][ny+dy[i]] == 0:
                    nx += dx[i]
                    ny += dy[i]
                if visited[nx][ny]:
                    continue
                visited[nx][ny] = True
                queue.append([nx, ny])
    
    def inBound(self, maze, x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0])
