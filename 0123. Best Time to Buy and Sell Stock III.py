"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

# We compute the two transactions separately via two passes: one forward and one backward.
# Local-Global Subarray. Time: O(n) with two passes, Space: O(1).
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        localMax = 0
        dp = [0] * n # dp[i] = max profit that can be made if sold at prices[i]
        curLow, curHigh = prices[0], prices[n-1]
        for i in range(1, n):
            curProfit = prices[i] - curLow
            localMax = max(localMax, curProfit)
            dp[i] = localMax
            curLow = min(curLow, prices[i])
        
        localMax = 0
        globalMax = dp[n-1] # initialize globalMax to be max profit if only buy-sell once
        for i in range(n-2, -1, -1):
            curProfit = curHigh - prices[i]
            localMax = max(localMax, curProfit)
            globalMax = max(globalMax, localMax + dp[i])
            curHigh = max(curHigh, prices[i])
        
        return globalMax
