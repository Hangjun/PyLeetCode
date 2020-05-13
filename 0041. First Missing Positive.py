"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""

# Similar to Problem 448. Find All Numbers Disappeared in an Array, we move every number val to its correct location nums[val-1].
# Two Pass. Time: O(n), Space: O(1).
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] <= n and nums[i] != i+1 and nums[nums[i]-1] != nums[i]:
                # CAUTION: doing the swap manually to avoid pointer errors
                tmp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = tmp
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1
