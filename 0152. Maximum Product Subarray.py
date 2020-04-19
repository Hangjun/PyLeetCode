"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

# Local-Global Subarray Problem. Time: O(n), Space: O(1).
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        localMax = localMin = globalMax = nums[0]
        for i in range(1, len(nums)):
            tmpLocalMax = localMax
            localMax = max(nums[i], tmpLocalMax * nums[i], localMin * nums[i])
            localMin = min(nums[i], tmpLocalMax * nums[i], localMin * nums[i])
            globalMax = max(globalMax, localMax)
        return globalMax
