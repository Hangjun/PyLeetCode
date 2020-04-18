"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
"""

# Exactly the same solution as the k = 2 case.
# Two Pointer Sliding Window + Hash Table. Time: O(n), Space: O(n).
from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        hist = defaultdict(int)
        count = 0 # count the number of indistinct characters
        res = 0
        for right in range(len(s)):
            hist[s[right]] += 1
            if hist[s[right]] == 1:
                # new character
                count += 1
            while count > k:
                hist[s[left]] -= 1
                if hist[s[left]] == 0:
                    count -= 1
                left += 1
            
            res = max(res, right-left+1)
        
        return res
