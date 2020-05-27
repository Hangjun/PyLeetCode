"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""

# Dynamic Programming + DFS. Time: O(mn), Space: O(mn).
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        # dp[i][j] = length of the longest increasing path FROM (i, j)
        dp = [[1 for _ in range(n)] for _ in range(m)]
        visited = [[False for _ in range(n)] for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                dp[i][j] = self.dfs(matrix, i, j, visited, dp)
                res = max(res, dp[i][j])
        return res
    
    def dfs(self, matrix, x, y, visited, dp):
        if visited[x][y]:
            return dp[x][y]
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if self.inBound(matrix, nx, ny) and matrix[nx][ny] > matrix[x][y]:
                dp[x][y] = max(dp[x][y], 1 + self.dfs(matrix, nx, ny, visited, dp))
        visited[x][y] = True
        return dp[x][y]
    
    
    def inBound(self, matrix, x, y):
        return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])
