"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""

# Stack. Time: O(m+n), Space: O(m+n).
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.process(S) == self.process(T)
    
    def process(self, s):
        stack = []
        for c in s:
            if c != '#':
                stack.append(c)
            else:
                if stack:
                    stack.pop()
        return stack
        
# Two Pointers. Time: O(m+n), Space: O(m+n). We can use iterator APIs in python to reduce the space complexity to O(1).
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.process(S) == self.process(T)
    
    def process(self, s):
        res = []
        skip = 0
        for c in reversed(s):
            if c == '#':
                skip += 1
            elif skip:
                skip -= 1
            else:
                res.append(c)
        return ''.join(res)

