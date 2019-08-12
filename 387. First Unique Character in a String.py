"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""

# Hash table. Time: O(n), Space: O(n)
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_dict = {}
        res = -1
        for c in s:
            s_dict[c] = s_dict.get(c, 0) + 1
        for i in range(len(s)):
            if s_dict[s[i]] == 1:
                res = i
                break
        return res
