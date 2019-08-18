"""
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
 

Example 2:

Input: 3
Output: False
"""

# Colliding Two Pointer. Time: O(n), Space: O(1).
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        l, r = 0, int(c ** 0.5)
        while l <= r:
            res = l ** 2 + r ** 2
            if res == c:
                return True
            elif res < c:
                l += 1
            else:
                r -= 1
        return False
