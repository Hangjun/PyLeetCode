"""
Given a 2-dimensional grid of integers, each value in the grid represents the color of the grid square at that location.

Two squares belong to the same connected component if and only if they have the same color and are next to each other in any of the 4 directions.

The border of a connected component is all the squares in the connected component that are either 4-directionally adjacent to a square not in the component, or on the boundary of the grid (the first or last row or column).

Given a square at location (r0, c0) in the grid and a color, color the border of the connected component of that square with the given color, and return the final grid.

 

Example 1:

Input: grid = [[1,1],[1,2]], r0 = 0, c0 = 0, color = 3
Output: [[3, 3], [3, 2]]
Example 2:

Input: grid = [[1,2,2],[2,3,2]], r0 = 0, c0 = 1, color = 3
Output: [[1, 3, 3], [2, 3, 3]]
Example 3:

Input: grid = [[1,1,1],[1,1,1],[1,1,1]], r0 = 1, c0 = 1, color = 2
Output: [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
 

Note:

1 <= grid.length <= 50
1 <= grid[0].length <= 50
1 <= grid[i][j] <= 1000
0 <= r0 < grid.length
0 <= c0 < grid[0].length
1 <= color <= 1000
"""

# Solution #1: DFS. First we find all the nodes in that component. Then we find the border nodes and color them. Time: O(mn), Space: O(mn).
class Solution(object):
    def colorBorder(self, grid, r0, c0, color):
        """
        :type grid: List[List[int]]
        :type r0: int
        :type c0: int
        :type color: int
        :rtype: List[List[int]]
        """
        if grid[r0][c0] == color:
            return grid
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for i in range(m)]
        # find all the nodes in the same component
        component = []
        self.dfs(grid, r0, c0, grid[r0][c0], visited, component)
        # find the border nodes of the component
        border = []
        for c in component:
            x, y = c
            dx = [-1, 0, 1, 0]
            dy = [0, 1, 0, -1]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not self.inBound(grid, nx, ny) or grid[nx][ny] != grid[r0][c0]:
                    border.append(c)
                    break
        for c in border:
            grid[c[0]][c[1]] = color
        return grid
        
    def dfs(self, grid, i, j, oldColor, visited, component):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and not visited[i][j] and grid[i][j] == oldColor:
            visited[i][j] = True
            component.append((i, j))
            self.dfs(grid, i-1, j, oldColor, visited, component)
            self.dfs(grid, i, j+1, oldColor, visited, component)
            self.dfs(grid, i+1, j, oldColor, visited, component)
            self.dfs(grid, i, j-1, oldColor, visited, component)
    
    def inBound(self, grid, i, j):
        return 0 <= i < len(grid) and 0 <= j < len(grid[0])

""" 
Solution #2: We can get border nodes and re-color DURING the DFS.
From the above, we see that a border node is a node that 1) lies in the same component of the original node and 2) it borders 
with either the boundary of the grid or a node that belongs to a _different_ component as the original node. Therefore, it is 
natural to think if we can pass both of these information DURING the DFS so that we can search AND re-color at the same time. 
It turns out that this can be done by returning a boolean (0 or 1) during the search that indiciate whether the current node 
is a border node. 

Let (i, j) be the node at the current DFS. If we have visited (i, j) before then we return 1. If (i, j) is out of bound or belongs 
to a different component, then we return 0. Returning a 1 indicates that the current node is a valid node and hence if all 
neighboring DFS search return 1 from the parent DFS run, then that parent node is NOT a border node. In another words, (i, j) is a 
border node iff dfs(i-1, j) + dfs(i, j+1) + dfs(i+1, j) + dfs(i, j-1) < 4. 

This relates whether (i, j) is a border node with the value of the its neighboring DFS calls.
"""
class Solution(object):
    def colorBorder(self, grid, r0, c0, color):
        """
        :type grid: List[List[int]]
        :type r0: int
        :type c0: int
        :type color: int
        :rtype: List[List[int]]
        """
        if grid[r0][c0] == color:
            return grid
        visited = set()
        
        def inBound(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        
        def dfs(i, j):
            if (i, j) in visited:
                return 1
            if not inBound(i, j) or grid[i][j] != grid[r0][c0]:
                return 0
            visited.add((i, j))
            if dfs(i-1, j) + dfs(i, j+1) + dfs(i+1, j) + dfs(i, j-1) < 4:
                # found a border node: safe to recolor on the fly
                grid[i][j] = color
            return 1
                
        dfs(r0, c0)
        return grid
