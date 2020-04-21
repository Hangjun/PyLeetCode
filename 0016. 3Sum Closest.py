"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

# Two Pointer. Time: O(n^2), Space: O(1).
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = None
        diff = sys.maxint
        n = len(nums)
        for i in range(n-2):
            left, right = i+1, n-1
            while left < right:
                curSum = nums[i] + nums[left] + nums[right]
                if curSum == target:
                    return curSum
                elif abs(curSum - target) < diff:
                    diff = abs(curSum - target)
                    res = curSum
                if curSum > target:
                    right -= 1
                else:
                    left += 1
        return res
