"""
Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example:

Input: nums = [-2,0,1,3], and target = 2
Output: 2 
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]
Follow up: Could you solve it in O(n2) runtime?
"""

"""
One caveat: when curSum < target, we need to increment left after the accouting. However, when curSum >= target, we need to 
decrement right.

Time: O(n^2), Space: O(1).
"""
class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = 0
        n = len(nums)
        if n < 3:
            return res
        nums.sort()
        for i in range(n-2):
            left, right = i+1, n-1
            while left < right:
                curSum = nums[i] + nums[left] + nums[right]
                if curSum < target:
                    res += right-left
                    left += 1                    
                else:
                    right -= 1
                
                    
        return res
