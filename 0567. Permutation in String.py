"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""

# Sliding Window. Time: O(n), Space: O(1).
from collections import defaultdict
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if (len(s1) > len(s2)):
            return False
        hist = defaultdict(int)
        for i in range(len(s1)):
            hist[s1[i]] += 1
            hist[s2[i]] -= 1
        if self._allZero(hist):
            return True
        
        # loop invariant: [j-len(s1), j-1] has been checked
        for j in range(len(s1), len(s2)):
            hist[s2[j-len(s1)]] += 1
            hist[s2[j]] -= 1
            if self._allZero(hist):
                return True
        
        return False
        
    def _allZero(self, hist):
        for _, value in hist.items():
            if value:
                return False
        return True
