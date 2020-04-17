"""
Given a string s and an integer k, find out if the given string is a K-Palindrome or not.

A string is K-Palindrome if it can be transformed into a palindrome by removing at most k characters from it.

 

Example 1:

Input: s = "abcdeca", k = 2
Output: true
Explanation: Remove 'b' and 'e' characters.
 

Constraints:

1 <= s.length <= 1000
s has only lowercase English letters.
1 <= k <= s.length
"""

"""
First idea that's too complicated:
Very naturally we think of dynamic programming. If part of the string is (k-1)-pal, then the remaining part only needs to be 
1-pal to make the entire string k-pal. Therefore I tempted to use dp[i][j][k] := whether s[i:j+1] is k-pal, k = 0, ..., k. This 
turns out to be too complicated and the running time is O(kn^2).

On the other hand, if the string s of length n is indeed k-pal, then there must exists a palindromic subsequence of length n-k. 
In another words, if we can find a palindromic subsequence of length at least n-k, then s is k-pal. This reduces the problem to 
finding the length of the LPS (subsequence) of s, which we know how to do.

Dynamic Programming. LPS. Time: O(n^2), Space: O(n^2).
"""
class Solution(object):
    def isValidPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        return self._lengthOfLPS(s) >= len(s)-k
    
    # compute the length of the longest palindromic subsequence
    def _lengthOfLPS(self, s):
        n = len(s)
        # dp[i][j] = len of LPS within s[i:j+1]
        dp = [[0 for i in range(n)] for j in range(n)]
        
        # initialize dp diagonally
        for i in range(n):
            dp[i][i] = 1
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = (0 if j == i+1 else dp[i+1][j-1]) + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        return dp[0][n-1]
