"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

# Two Pointers, 1-pass. Time: O(n), Space: O(1)
from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (len(s) <= 1):
            return len(s)
            
        used = {}
        start, res = 0, 1
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                # update start to jump over the duplicating character's most recent location
                start = used[c] + 1
            else:
                res = max(res, i - start + 1)
            # update the most recent location index for character c
            used[c] = i
        return res
