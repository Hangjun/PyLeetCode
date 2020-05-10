"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

# Iteratively pop the last digit and push it onto the res. Time: O(n), Space: O(n).
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        negative = False
        if x < 0:
            negative = True
            x = -x
        # we repeatedly pop the last digit of the input and push it onto the res
        while x > 0:
            pop = x % 10
            x /= 10
            res = res * 10 + pop
        
        if res > (2 ** 31 - 1):
            return 0
        return -1 * res if negative else res
