"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
"""

"""
We can either have the convention of partialSum[i] = nums[0] + ... + nums[i] or partialSum[i] = nums[0] + ... + nums[i-1]. We will 
go with the second convention for majority of these range query problems.

Time: O(n) to construct, O(1) to serve. Space: O(n).
"""
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.partialSum = [0 for _ in range(len(nums)+1)]
        # partialSum[i] = sum(nums[0...i-1]), the sum of the first i numbers
        for i in range(len(nums)):
            self.partialSum[i+1] = self.partialSum[i] + nums[i]
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.partialSum[j+1] - self.partialSum[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
