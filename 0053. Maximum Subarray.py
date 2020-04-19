"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

# Local-Global Subarray Problem. Time: O(n), Space: O(1).
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curSum, res = -sys.maxint-1, -sys.maxint-1
        for n in nums:
            curSum = max(curSum + n, n)
            res = max(res, curSum)
        return res
