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

"""
We all know how to check a string of parentheses is valid using a stack. Or even simpler use a counter.
The counter will increase when it is ‘(‘ and decrease when it is ‘)’. Whenever the counter is negative, we have more ‘)’ than 
‘(‘ in the prefix.

To make the prefix valid, we need to remove a ‘)’. The problem is: which one? The answer is any one in the prefix. However, if 
we remove any one, we will generate duplicate results, for example: s = ()), we can remove s[1] or s[2] but the result is the 
same (). Thus, we restrict ourself to remove the first ) in a series of concecutive )s.

After the removal, the prefix is then valid. We then call the function recursively to solve the rest of the string. However, 
we need to keep another information: the last removal position. If we do not have this position, we will generate duplicate by 
removing two ‘)’ in two steps only with a different order.
For this, we keep tracking the last removal position and only remove ‘)’ after that.

Now one may ask. What about ‘(‘? What if s = ‘(()(()’ in which we need remove ‘(‘?
The answer is: do the same from right to left.
However a cleverer idea is: reverse the string and reuse the code!
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
