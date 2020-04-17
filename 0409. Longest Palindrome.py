"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""

"""
Algorithm:
1. Build histogram.
2. For even occuring characters, add up their occurrences.
3. For odd occuring characters, add up their occurrences - 1.
4. If there is at least one odd occuring character, plus 1 to the final result and return.

Time: O(n), Space: O(n).
"""
from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hist = Counter(s)
        res = 0
        one = 0
        for value in hist.values():
            if value % 2 == 0:
                res += value
            else:
                res += value-1
                one = 1
        return res + one
