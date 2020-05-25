"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""

# Time: O(mn), Space: O(mn).
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        # dp[i][j] = isMatch(s[:i], p[:j]), exclusive
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True # empty string matches with empty pattern
        # initialize dp[0][j] : pattern matching empty string
        for j in range(1, n+1):
            dp[0][j] = j > 1 and p[j-1] == '*' and dp[0][j-2]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] != '*':
                    dp[i][j] = (s[i-1] == p[j-1] or p[j-1] == '.') and dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-2] or ((s[i-1] == p[j-2] or p[j-2] == '.') and dp[i-1][j])
        
        return dp[m][n]
