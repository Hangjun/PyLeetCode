"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
"""

# Similar to https://github.com/Hangjun/PyLeetCode/blob/master/0076.%20Minimum%20Window%20Substring.py. 
# Two Pointer Sliding Window. Time: O(n), Space: O(1).
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        curSum = 0
        minLen = sys.maxint
        for right, n in enumerate(nums):
            curSum += n
            while curSum >= s:
                if right-left+1 < minLen:
                    minLen = right-left+1
                curSum -= nums[left]
                left += 1
        return minLen if minLen < sys.maxint else 0
