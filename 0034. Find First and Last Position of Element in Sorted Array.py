"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

# Two Pass Binary Search. Time: O(logn), Space: O(1)
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        lower = self.findLowerBound(nums, target)
        upper = self.findUpperBound(nums, target)
        if lower <= upper:
            return [lower, upper]
        else:
            return [-1, -1]
        
    def findLowerBound(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) / 2
            if (nums[mid] < target):
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    def findUpperBound(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) / 2
            if (nums[mid] > target):
                right = mid - 1
            else:
                left = mid + 1
        return right
