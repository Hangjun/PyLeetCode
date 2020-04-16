"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Note:

The input string length won't exceed 1000.
"""

"""
The bruteforce algorithm will look at all the O(n^2) pairs of (start, end) indices and spend O(n) to determine s[start, end+1]
is a palindrome. We can use dynamic programming to achieve O(1) time to determine this. So the total running time is O(n^2).

We can further improve to have O(n) time by using Manacher's algorithm.

Note that the solution is actually a very useful subroutine for other problems to quickly look up whether a given slice of a 
string is a palindrome or not, e.g. Palindrome partitions.
"""
# Dynamic Programming. Time: O(n^2), Space: O(n^2).
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        count = 0
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = 1
                    count += 1
        return count


