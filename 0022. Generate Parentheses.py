"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

# Backtracking: Time: O(4^n), Space: O(4^n).
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.dfs("", 0, 0, n, res)
        return res
    
    def dfs(self, cur, openCount, closeCount, n, res):
        # terminating condition
        if len(cur) == n * 2:
            res.append(cur)
            return
        
        # dfs on the neighboring states
        if openCount < n:
            self.dfs(cur + "(", openCount+1, closeCount, n, res)
        if closeCount < openCount:
            self.dfs(cur + ")", openCount, closeCount+1, n, res)
