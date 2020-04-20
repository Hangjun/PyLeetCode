"""
Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
"""

"""
Very naturally a Dynamic Programming problem. We again use the local-global set up. We define local[i][j] = max profit until i 
with j transactions such that we sell on the ith day. This is our local optimal. Global[i][j] is then the max profit until day i 
with j transactions. To derive at the state transfer function, note that on the ith day, we can either have completed j-1 
transactions until day i-1, and perform the jth transaction on the ith day (gloabl[i-1][j-1] + max(curProfit, 0)), or we can 
continue the jth transaction from day i-1: local[i-1][j] + delta. The global[i][j] is also the max of these two options:
global[i][j] = max(local[i][j], global[i-1][j]).

Time: O(nk), Space: O(nk).
"""
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        if k >= n:
            return self.maxProfitUnlimited(prices)
        # local[i][j] = max profit until day i with j transactions with a sell on day i
        local = [[0 for i in range(k+1)] for j in range(n)]
        # res[i][j] = max profit until day i with j transactions
        res = [[0 for i in range(k+1)] for j in range(n)]
        for i in range(1, n):
            delta = prices[i] - prices[i-1]
            for j in range(1, k+1):
                local[i][j] = max(res[i-1][j-1] + max(delta, 0), local[i-1][j] + delta) # a new transaction or a continued transaction
                res[i][j] = max(local[i][j], res[i-1][j]) # transaction at i or no transaction at i
        
        return res[n-1][k]
    
    def maxProfitUnlimited(self, prices):
        res = 0
        for i in range(1, len(prices)):
            res += max(0, prices[i] - prices[i-1])
        return res

# We can improve the space complexity to O(k) using standard rolling array trick.
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        if k >= n:
            return self.maxProfitUnlimited(prices)
        # local[i][j] = max profit until day i with j transactions with a sell on day i
        local = [[0 for i in range(k+1)] for j in range(2)]
        # res[i][j] = max profit until day i with j transactions
        res = [[0 for i in range(k+1)] for j in range(2)]
        for i in range(1, n):
            delta = prices[i] - prices[i-1]
            for j in range(1, k+1):
                local[i%2][j] = max(res[(i-1)%2][j-1] + max(delta, 0), local[(i-1)%2][j] + delta)
                res[i%2][j] = max(local[i%2][j], res[(i-1)%2][j])
        
        return res[(n-1)%2][k]
    
    def maxProfitUnlimited(self, prices):
        res = 0
        for i in range(1, len(prices)):
            res += max(0, prices[i] - prices[i-1])
        return res

