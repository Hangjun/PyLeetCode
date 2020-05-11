"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:

Input:  "69"
Output: true
Example 2:

Input:  "88"
Output: true
Example 3:

Input:  "962"
Output: false
"""

# Hash Table. Collision Two Pointers. Time: O(n), Space: O(1).
class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dict = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        left, right = 0, len(num)-1
        while left <= right:
            if num[left] not in dict or dict[num[left]] != num[right]:
                return False
            left += 1
            right -= 1
        return True
