"""
Given two strings s and t, determine if they are both one edit distance apart.

Note: 

There are 3 possiblities to satisify one edit distance apart:

Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t
Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "cab", t = "ad"
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:

Input: s = "1203", t = "1213"
Output: true
Explanation: We can replace '0' with '1' to get t.
"""

# Time: O(n), Space: O(1).
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            return self.isOneEditDistance(t, s)
        if len(t) - len(s) > 1:
            return False
        i = j = 0
        hasDiffered = False
        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                if hasDiffered:
                    return False
                hasDiffered = True
                if len(s) < len(t):
                    i -= 1
            i += 1
            j += 1
        return hasDiffered or len(s) < len(t)
