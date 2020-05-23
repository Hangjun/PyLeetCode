"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""

# DFS. Time: O(2^n), Space: O(2^n).
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self._remove(s, res, 0, 0, '(', ')')
        return res
    
    def _remove(self, s, res, i_start, j_start, open_paren, close_paren):
        num_open = num_close = 0
        for i in range(i_start, len(s)):
            if s[i] == open_paren:
                num_open += 1
            if s[i] == close_paren:
                num_close += 1
            if num_close > num_open:
                for j in range(j_start, i+1):
                    if s[j] == close_paren and (j == j_start or s[j-1] != close_paren):
                        self._remove(s[:j] + s[j+1:], res, i, j, open_paren, close_paren)
                return
        
        s_reverse = s[::-1]
        if open_paren == '(':
            self._remove(s_reverse, res, 0, 0, ')', '(')
        else:
            res.append(s_reverse)
