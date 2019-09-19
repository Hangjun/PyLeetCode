"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
"""

# Hash Table. Time: O(n), Space: O(n).
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        forward, backward = {}, {}
        for i in range(len(s)):
            if s[i] not in forward:
                forward[s[i]] = t[i]
            elif forward[s[i]] != t[i]:
                return False
            
            if t[i] not in backward:
                backward[t[i]] = s[i]
            elif backward[t[i]] != s[i]:
                return False
        return True

# Here is another implementation of the same algorithm using Python's map function:
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return map(s.find, s) == map(t.find, t)
