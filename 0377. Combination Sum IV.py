"""
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
 

Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
"""

"""
Analysis: This problem is very similar to the Part I of Combination Sum. However, here we are only returning the number of combinations to sum to a target, not the actual combinations. If we use the same DFS approach as in Part I, we will get TLE.
The key to this problem is to notice that, suppose n1 + n2 + n3 = target, where n1, n2 and n3 are from nums, then:
# combinations to sum to target += # combinations to sum to n1 + # combinations to sum to n2 + # combinations to sum to n3. 
From here, it is pretty obvious that the solution should be DP. Define dp[i] := # combinations sums up to i, we can compute dp[target] either from the top-down, or bottom-up. This problem is also very similar the the "Climing up the Stairs problem".

Dynamic Programming. Time: O(n), Space: O(n)
"""
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # dp[i] = # combinations adding up to i
        dp = [0] * (target+1)
        dp[0] = 1 # basecase: there is one way to add up to 0: []
        for i in range(1, target+1):
            for n in nums:
                if i >= n:
                    dp[i] += dp[i-n]
        return dp[target]
