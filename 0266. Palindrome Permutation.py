"""
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
"""

# Hash Table to record the histogram. Time: O(n). Space: O(n).
from collections import defaultdict
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hist = defaultdict(int)
        for c in s:
            if hist[c] > 0:
                hist[c] -= 1
            else:
                hist[c] += 1
        curSum = 0
        for key, value in hist.items():
            curSum += value
        return curSum < 2

# We can also use Python's Counter data structure:
from collections import Counter
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return len([i for i in Counter(s).values() if i % 2 != 0]) < 2
