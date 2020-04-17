"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

"""
Solution #1: Dynamic Programming. Time: O(n^2), Space: O(n^2). We simply apply the Joseki of Palindromic Substrings and compute 
for each slice of substring s[i:j] whether it is a palindrome using dynamic programming.
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [[0 for i in range(n)] for j in range(n)]
        maxLen = 0
        startIndex, endIndex = 0, 0
        # Joseki for computing whether a given slice s[i:j+1] is a Palindrome or not
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i<=2 or dp[i+1][j-1]):
                    dp[i][j] = 1
                    if j-i+1 > maxLen:
                        maxLen = j-i+1
                        startIndex = i
                        endIndex = j
        return s[startIndex:endIndex+1]

"""
Solution #2: We can improve on the space complexity. The idea is to, for every character in the string, check how long a 
palindromic substring can it expand to with it being its center. What is the total number of such centers given that there are 
n characters in the string? The answer is 2n+1, not n, since there is a possible center between any two consecutive characters 
(think about the case where a palindromic subtring has even number of characters).
Time: O(n^2), Space: O(1).
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        res = ""
        for i in range(len(s)):
            odd = self._expand(s, i, i)
            if len(odd) > len(res):
                res = odd
            even = self._expand(s, i, i+1)
            if len(even) > len(res):
                res = even
        return res
            
    
    # Compute the longest expandable palindromic subbstring from left and right indices within s
    def _expand(self, s, left, right):
        # loop invariant: (left, right) is palindromic
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1: right]
        
# We can further improve the time complexity to O(n) by using the Manachers Algorithm with O(n).
