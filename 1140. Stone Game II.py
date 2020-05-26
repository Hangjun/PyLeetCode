"""
Alex and Lee continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

Alex and Lee take turns, with Alex starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alex and Lee play optimally, return the maximum number of stones Alex can get.

 

Example 1:

Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alex takes one pile at the beginning, Lee takes two piles, then Alex takes 2 piles again. Alex can get 2 + 4 + 4 = 10 piles in total. If Alex takes two piles at the beginning, then Lee can take all three piles left. In this case, Alex get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
 

Constraints:

1 <= piles.length <= 100
1 <= piles[i] <= 10 ^ 4
"""

# Dynamic Programming. Time: O(nm^2), Space: O(nm).
class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)
        suffix_sum = [0 for _ in range(n)]
        suffix_sum[n-1] = piles[n-1]
        for i in range(n-2, -1, -1):
            suffix_sum[i] = piles[i] + suffix_sum[i+1]
        
        # dp[i][m] = maximum number of stones to get at index i and with M = m
        dp = [[0 for _ in range(n)] for _ in range(n)]
        # we work our way backwards: dp[i][m] = max(suffix_sum[i] - dp[i+x][max(m, x)]) for 1 <= x <= 2*m
        for i in range(n-1, -1, -1):
            for m in range(n-1, 0, -1):
                for x in range(1, 2*m+1):
                    if i+x >= n: # just take all the rest
                        dp[i][m] = max(dp[i][m], suffix_sum[i])
                    else:
                        dp[i][m] = max(dp[i][m], suffix_sum[i] - dp[i+x][max(m, x)])
        
        return dp[0][1]
