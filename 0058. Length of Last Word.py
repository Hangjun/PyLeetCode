"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""

# Time: O(n), Space: O(1). Only caveat is to handle trailing spaces.
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        p, res = len(s)-1, 0
        while p >= 0:
            if s[p] != ' ':
                res += 1
            # we are at the end of the last word
            elif res > 0:
                return res
            p -= 1
        return res
