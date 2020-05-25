"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""

# Dynamic Programming. Time: O(n), Space: O(n) - can be easily optimized to O(1) using rolling array trick.
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # handle corner cases where len(s) < 2
        if not s:
            return 0
        if len(s) == 1:
            return int(self.validOne(s))
        if not self.validOne(s[0]):
            return 0
        
        # we handle the remaining cases with len(s) >= 2
        # dp[i] := number of ways to decode s[0...i]
        dp = [0 for _ in range(len(s))]
        
        # need to initialize dp[0] and dp[2]
        dp[0] = 1
        if self.validOne(s[1]):
            dp[1] = 1
            if self.validTwo(s[0], s[1]):
                dp[1] += 1
        else:
            if self.validTwo(s[0], s[1]):
                dp[1] = 1
            else:
                return 0
        print dp
        # state transition: dp[i] depends on the state of s[i-1] and s[i]
        for i in range(2, len(s)):
            if self.validOne(s[i]) and self.validTwo(s[i-1], s[i]):
                dp[i] = dp[i-1] + dp[i-2]
            elif self.validOne(s[i]):
                dp[i] = dp[i-1]
            elif self.validTwo(s[i-1], s[i]):
                dp[i] = dp[i-2]
            else:
                return 0
            
        return dp[len(s)-1]
        
        
    def validOne(self, c):
        return ord('1') <= ord(c) <= ord('9')
    
    def validTwo(self, a, b):
        return a == '1' or (a == '2' and ord('0') <= ord(b) <= ord('6'))
