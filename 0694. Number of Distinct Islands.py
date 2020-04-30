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

# DFS: Time: O(mn), Space: (mn) assuming we cannot modify input. The idea is to record the DFS traverse path.
class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(i, j, path):
            if 0 <= i < m and 0 <= j < n and not visited[i][j] and grid[i][j] == 1:
                visited[i][j] = True
                path += dfs(i+1, j, "d")
                path += dfs(i, j+1, "r")
                path += dfs(i-1, j, "u")
                path += dfs(i, j-1, "l")
                return path + "b" # must include the backtrack step to have the complete trace recorded
            return ""
        
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        visited = [[False for i in range(n)] for j in range(m)]
        contour = set()
        for i in range(m):
            for j in range(n):
                # we do not need to have "" contours
                if not visited[i][j] and grid[i][j] == 1:
                    contour.add(dfs(i, j, "o"))
        return len(contour)

