"""
Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
 

Constraints:

1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.
"""

# Solution #1: Use stack to find miss-matching parentheses. Time: O(n), Space: O(n).
class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        indices_to_remove = set()
        for i, c in enumerate(s):
            if c not in "()":
                continue
            if c == "(":
                stack.append(i)
            elif not stack:
                indices_to_remove.add(i)
            else:
                stack.pop()
        indices_to_remove = indices_to_remove.union(set(stack))
        res = []
        for i, c in enumerate(s):
            if i not in indices_to_remove:
                res.append(c)
        return "".join(res)
        
# Solution #2: Use string reverse to find miss-matching paraentheses. Time: O(n), Space: O(n).
class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        def remove(s, open_char, close_char):
            res = []
            balance = 0
            for c in s:
                if c == open_char:
                    balance += 1
                if c == close_char:
                    if balance == 0:
                        continue
                    balance -= 1
                res.append(c)
            return "".join(res)
        
        s = remove(s, "(", ")")
        s = remove(s[::-1], ")", "(")
        return s[::-1]
