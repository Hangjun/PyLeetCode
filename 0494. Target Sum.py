"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
"""

# This is a 0/1 Knapsack problem. Dynamic Programming. Time: O(n^2), Space: can be optimized to O(n) using rolling array.
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        total_sum = sum(nums)
        if S < -total_sum or S > total_sum:
            return 0
        # dp[i][j] = number of ways to reach j-sum with the first i numbers nums[0...i-1]
        dp = [[0 for _ in range(2 * total_sum + 2)] for _ in range(len(nums)+1) ]
        dp[0][total_sum] = 1 # there exists a unique way to sum to 0 with no number
        
        for i in range(1, len(nums)+1):
            for j in range(2*total_sum+1):
                if j + nums[i-1] < 2 * total_sum + 1:
                    dp[i][j] += dp[i-1][j+nums[i-1]]
                if j - nums[i-1] >= 0:
                    dp[i][j] += dp[i-1][j-nums[i-1]]
        
        return dp[len(nums)][S+total_sum]
        
