"""
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. 
             Minimum cost: 2 + 5 + 3 = 10.
"""

# Dynamic Programming. Time: O(m), Space: O(m). m = number of houses.
class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0
        m, n = len(costs), len(costs[0])
        # dp[i][j] = min cost of paint up to the ith house such that the ith house is painted with color j
        # dp[i][j] = min(dp[i-1][k], k != j) + cost[i][k]
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0] = costs[0]
        for i in range(1, m):
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]
        
        return min(dp[m-1][0], dp[m-1][1], dp[m-1][2])
        
# We can improve the space complexity to O(1) by using the rolling matrix trick:
class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0
        m, n = len(costs), len(costs[0])
        # dp[i][j] = min cost of paint up to the ith house such that the ith house is painted with color j
        # dp[i][j] = min(dp[i-1][k], k != j) + cost[i][k]
        dp = [[0 for _ in range(n)] for _ in range(2)]
        dp[0] = costs[0]
        for i in range(1, m):
            dp[i%2][0] = min(dp[(i-1)%2][1], dp[(i-1)%2][2]) + costs[i][0]
            dp[i%2][1] = min(dp[(i-1)%2][0], dp[(i-1)%2][2]) + costs[i][1]
            dp[i%2][2] = min(dp[(i-1)%2][0], dp[(i-1)%2][1]) + costs[i][2]
        
        return min(dp[(m-1)%2][0], dp[(m-1)%2][1], dp[(m-1)%2][2])
