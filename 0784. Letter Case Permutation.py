"""
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
"""

# This problem is a simple variation of https://leetcode.com/problems/letter-combinations-of-a-phone-number/. We can either use 
backtracking DFS or iterative construction. We present both solutions.
# Solution #1: Backtracking DFS.
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        self.dfs(S, 0, "", res)
        return res
    
    def dfs(self, S, start, path, res):
        if start == len(S):
            res.append(path)
            return
        if S[start].isdigit():
            self.dfs(S, start+1, path + S[start], res)
        else:
            for c in [S[start].lower(), S[start].upper()]:
                self.dfs(S, start+1, path + c, res)
            
# Solution #2: Iterative.
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = [""]
        for c in S:
            if c.isalpha():
                res = [a + b for a in res for b in [c.lower(), c.upper()]]
            else:
                res = [a + c for a in res]
        return res
