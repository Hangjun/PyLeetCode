"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.

"""

# Binary Search. Time: O(logn), Space: O(1).
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x == 1:
            return 1
        l, r = 0, int(math.ceil(x/2))
        # loop invariant: solution lies within [l-1, r]
        while l <= r:
            mid = l + (r - l) / 2
            midSquare = mid * mid
            if midSquare == x:
                return mid
            elif midSquare < x:
                l = mid + 1
            else:
                r = mid - 1
        
        # l == r + 1
        return r

# A different (more consise implementation)
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x == 1:
            return 1
        l, r = 1, int(math.ceil(x/2))
        while True:
            mid = l + (r - l) / 2
            if (mid > x / mid):
                r = mid -1
            else:
                if ((mid + 1) > x / (mid + 1)):
                    return mid
                else:
                    l = mid+1
