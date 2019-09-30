"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.
Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.
Note: The length of each dimension in the given grid does not exceed 50.
"""

# DFS: Time: O(mn), Space: (mn) assuming we cannot modify input. The idea is to record the entire DFS path.
class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(i, j, visited, path):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and not visited[i][j] and grid[i][j] == 1:
                visited[i][j] = True
                # compute the entire DFS path
                return path \
                + dfs(i-1, j, visited, "u") + "d" \
                + dfs(i, j+1, visited, "r") + "l" \
                + dfs(i+1, j, visited, "d") + "u" \
                + dfs(i, j-1, visited, "l") + "r"
            else:
                return ""
            
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for i in range(m)]
        island_contours = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    island_contours.add(dfs(i, j, visited, "s"))
        return len(island_contours)

# A different DFS implementation:
class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(i, j, visited, move):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and not visited[i][j] and grid[i][j] == 1:
                visited[i][j] = True
                self.path += move
                dfs(i-1, j, visited, "u")
                dfs(i, j+1, visited, "r")
                dfs(i+1, j, visited, "d")
                dfs(i, j-1, visited, "l")
                self.path += "b"
            else:
                return ""
            
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for i in range(m)]
        island_contours = set()
        self.path = ""
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    dfs(i, j, visited, "0")
                    island_contours.add(self.path)
                    print "contour = ", self.path
                    self.path = ""
        return len(island_contours)
