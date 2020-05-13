"""
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.
"""

# Two Pointer. Time: O(n), Space: O(1). In-place.
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left = -1
        # invariant: [0, left] = does not contain val; [left+1, right-1] = val, [right, n-1] = unexplored
        for right in range(len(nums)):
            if nums[right] == val:
                continue
            left += 1
            nums[left], nums[right] = nums[right], nums[left]
        return left + 1
        
