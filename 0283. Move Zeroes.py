"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
# Two Pointers. Time: O(n), Space: O(1). In-place.
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        # invariant: [0, left) = no zero, [left, right) = zeros, [right, n-1] = unexplored
        for right in range(len(nums)):
            if not nums[right]:
                continue
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
