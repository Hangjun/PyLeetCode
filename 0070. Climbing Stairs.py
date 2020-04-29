"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

# DP. Time: O(n), Space: O(1).
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        # dp[i] = number of ways to reach level i
        dp = [0 for i in range(3)]
        
        # initialization
        dp[0 % 3] = 1
        dp[1 % 3] = 1
        
        for i in range(2, n+1):
            dp[i % 3] = dp[(i-1) % 3] + dp[(i-2) % 3]
        
        return dp[n % 3]
