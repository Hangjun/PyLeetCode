"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""

# Greedy Algorithm, Time: O(n), Space: O(1)
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_pal_range(i, j):
            while (i < j):
                if (s[i] != s[j]):
                    return False
                i += 1
                j -= 1
            return True
        
        l, r = 0, len(s)-1
        while (l < r):
            if (s[l] == s[r]):
                l += 1
                r -= 1
            else:
                return is_pal_range(l+1, r) or is_pal_range(l, r-1)
        return True
