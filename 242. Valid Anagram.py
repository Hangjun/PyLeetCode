"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

# Hash table. Time: O(n), Space: O(n) - actually O(1) since there are 26 distinct characters in total.
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s) != len(t)):
            return False
        dict = {}
        for a in s:
            dict[a] = dict.get(a, 0) + 1
        for b in t:
            if b not in dict:
                return False
            dict[b] -= 1
            if dict[b] < 0:
                return False
        return True
