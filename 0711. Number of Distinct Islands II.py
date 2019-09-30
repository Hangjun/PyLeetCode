"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if they have the same shape, or have the same shape after rotation (90, 180, or 270 degrees only) or reflection (left/right direction or up/down direction).

Example 1:
11000
10000
00001
00011
Given the above grid map, return 1.

Notice that:
11
1
and
 1
11
are considered same island shapes. Because if we make a 180 degrees clockwise rotation on the first island, then two islands will have the same shapes.
Example 2:
11100
10001
01001
01110
Given the above grid map, return 2.

Here are the two distinct islands:
111
1
and
1
1

Notice that:
111
1
and
1
111
are considered same island shapes. Because if we flip the first array in the up/down direction, then they have the same shapes.
Note: The length of each dimension in the given grid does not exceed 50.
"""

# DFS solution. The key is to standardize the normalization of each island and return the canonical representation of each island. We can then just comapre the canonical representation to de-dup.
class Solution(object):
    def numDistinctIslands2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for i in range(m)]
        island_shapes = set()
        for i in range(m):
            for j in range(n):
                contour = []
                if grid[i][j] == 1 and not visited[i][j]:
                    self.dfs(grid, i, j, visited, contour)
                    normalized_contour = self.normalize(contour)
                    island_shapes.add(normalized_contour)
        return len(island_shapes)
    
    def dfs(self, grid, i, j, visited, contour):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and not visited[i][j] and grid[i][j] == 1:
            visited[i][j] = True
            contour.append((i, j))
            self.dfs(grid, i-1, j, visited, contour)
            self.dfs(grid, i, j+1, visited, contour)
            self.dfs(grid, i+1, j, visited, contour)
            self.dfs(grid, i, j-1, visited, contour)
    
    def normalize(self, contour):
        rotated_contours = [[] for _ in range(8)]
        normalized_contours = []
        for c in contour:
            x, y = c
            rotated_contours[0].append((x, y))
            rotated_contours[1].append((-x, y))
            rotated_contours[2].append((x, -y))
            rotated_contours[3].append((-x, -y))
            rotated_contours[4].append((y, x))
            rotated_contours[5].append((-y, x))
            rotated_contours[6].append((y, -x))
            rotated_contours[7].append((-y, -x))
        
        for rc in rotated_contours:
            rc.sort()
          
        # normailize to get relative coordinates with respect to first node
        for rc in rotated_contours:
            tmp = [(0, 0)]
            for i in range(1, len(rc)):
                tmp.append((rc[i][0] - rc[0][0], rc[i][1] - rc[0][1]))
            normalized_contours.append(tmp[:])
        
        normalized_contours.sort() # to get the canonical representation
        return tuple(normalized_contours[0]) # for hashing purposes
