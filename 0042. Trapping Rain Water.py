"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

# Two Pointer Sliding Window. Time: O(n), Space: O(1).
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height)-1
        water = 0
        while left < right:
            # pour water from the lower side
            if height[left] < height[right]:
                leftBound = height[left]
                while left < right and height[left] <= leftBound:
                    water += leftBound - height[left]
                    left += 1
            else:
                rightBound = height[right]
                while left < right and height[right] <= rightBound:
                    water += rightBound - height[right]
                    right -= 1
        return water
