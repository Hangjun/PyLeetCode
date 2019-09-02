"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""

# Two Pointers. Sliding Window. Two Pass. Time: O(n), Space: O(n).
from collections import defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ""
        need_to_find = defaultdict(int)
        has_found = defaultdict(int)
        for c in t:
            need_to_find[c] += 1
        res, min_len = None, sys.maxint
        left, count = 0, 0
        for right, c in enumerate(s):
            if c not in need_to_find:
                continue
            # c is a character needed
            if has_found[c] < need_to_find[c]:
                count += 1
            has_found[c] += 1
            # once we have found all of t's characters, we shrink the left pointer
            if (count == len(t)):
                while s[left] not in need_to_find or has_found[s[left]] > need_to_find[s[left]]:
                    if s[left] in need_to_find and has_found[s[left]] > need_to_find[s[left]]:
                        has_found[s[left]] -= 1
                    left += 1
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = s[left:right+1]
                    print "update res = ", res
        
        return res if res else ""
