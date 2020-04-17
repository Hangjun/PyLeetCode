"""
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
"""

"""
Whenever we going from substring to subsequence, it usually works by modifying the definition of the DP. Typically we need to 
change the DP to measure a continuous quantity to a non-continuous one. In this case, we need to compute the length of the LPS 
(subsequence), it is natural to transform dp[i][j] to measure a property of a continuous substring s[i:j+1] to a non-continous 
property, in this case dp[i][j] should represent the length of the LPS (subsequence) within s[i:j+1].

Dynamic Programming. Time: O(n^2), Space: O(n^2).
"""
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # dp[i][j] := length of LPS in s[i:j+1]
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = 1
            
        # work the DP from the bottom right to top and left
        for i in range(n-1, -1,  -1):
            for j in range(i+1, n): # notice that j starts from i+1 since we have already initialized dp[i][j]
                if s[i] == s[j]:
                    dp[i][j] = (0 if j == i + 1 else dp[i+1][j-1]) + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        return dp[0][n-1]
