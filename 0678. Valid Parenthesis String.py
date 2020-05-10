"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].
"""

# Greedy Algorithm. Time: O(n), Space: O(1).
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lo = hi = 0
        for c in s:
            lo += 1 if c == '(' else -1
            hi += 1 if c != ')' else -1
            if hi < 0:
                return False
            lo = max(lo, 0)
        return lo == 0

"""
The above greedy algorithm is very difficult to come by during interviews. We go back to the basics. This problem has a wildcard 
matching flavor, which suggests that we might be able to use a dynamic programming algorithm. We can define dp[i][j] as whether 
the substring s[i:j+1] is valid. This particular DP progresses along the perpendicular direction of the upper right diagnoals, 
which is interesting to learn as well.

Dynamic Programming. Time: O(n^3), Space: O(n^2).
"""
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        LEFT = "(*"
        RIGHT = "*)"
        n = len(s)
        # dp[i][j] = whether s[i:j+1] is valid
        dp = [[False for i in range(n)] for j in range(n)]
        
        # initialize the diagnoal that corresponds to 1-grams and 2-grams of the string
        for i in range(n):
            if s[i] == '*':
                dp[i][i] = True
            if i < n-1 and s[i] in LEFT and s[i+1] in RIGHT:
                dp[i][i+1] = True
        
        # state transfer to compute the validity of the k-grams
        # upshot: DP progresses along the perpendicular direction of the diagonals
        for k in range(2, n):
            # i + k <= n-1, i.e. i <= n-k-1
            for i in range(n-k):
                if s[i] == '*' and dp[i+1][i+k] == True:
                    dp[i][i+k] = True
                elif s[i] in LEFT: # look for a middle point c in [i, i+k] that is in RIGHT
                    for c in range(i+1, i+k+1):
                        # check s[i+1 ... c-1] and s[c+1 ... i+k]
                        if (s[c] in RIGHT) and (c == i+1 or dp[i+1][c-1]) and (c == i+k or dp[c+1][i+k]):
                            dp[i][i+k] = True
        
        return dp[0][n-1]
