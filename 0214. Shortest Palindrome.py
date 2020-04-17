"""
Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: "abcd"
Output: "dcbabcd"
"""

# KMP. Time: O(n), Space: O(n).
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        t = s[::-1]
        lpsPrefixLen = self._computeLPSPrefixLen(s + "#" + t)
        if lpsPrefixLen == len(s):
            return s
        suffix = s[lpsPrefixLen:]
        print(suffix)
        return suffix[::-1] + s
        
    def _computeLPSPrefixLen(self, s):
        n = len(s)
        next = [-1] * n
        j = -1
        for i in range(1, n):
            while j >= 0 and s[i] != s[j+1]:
                j = next[j]
            if s[i] == s[j+1]:
                j += 1
                next[i] = j
        
        return next[n-1]+1
