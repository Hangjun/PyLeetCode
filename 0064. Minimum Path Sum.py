"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

# Standard Dynamic Programming. Time: O(mn), Space: O(mn).
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        if not m or not n:
            return 0
        # dp[i][j] = min path sum to reach grid[i][j]
        dp = [[sys.maxint for i in range(n)] for j in range(m)]
        
        # initialize the boundary, dp[0, :] and dp[:, 0]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
            
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
        return dp[m-1][n-1]

# We can optimize the space complexity to be O(min(m, n)) with only one row/column needed.
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        if not m or not n:
            return 0
        # WLOG we go with a row
        dp = [sys.maxint for i in range(n)] 
        
        # initialize first row
        dp[0] = grid[0][0]
        for j in range(1, n):
            dp[j] = dp[j-1] + grid[0][j]
            
        for i in range(1, m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j]

        return dp[n-1]
