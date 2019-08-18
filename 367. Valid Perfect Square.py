"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
"""

# Binary Search. Very similar to sqrt(num). Time: O(logn), Space: O(1).
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        l, r = 1, int(math.ceil(num/2))
        while l <= r:
            mid = l + (r - l) / 2
            midSquare = mid * mid
            if midSquare == num:
                return True
            elif midSquare < num:
                l = mid + 1
            else:
                r = mid - 1
        return False
