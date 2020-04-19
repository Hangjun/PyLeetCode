"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""

# A typical two pointer sliding window implementation: Time: O(n), Space: O(1).
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = -1
        right = 0
        res = 0
        while right < len(nums):
            while right < len(nums) and nums[right] != 1:
                right += 1
            if right == len(nums):
                return res
            left = right
            while right < len(nums) and nums[right] == 1:
                right += 1
            res = max(res, right-left)
        return res

# We can make the implementation simplier. Time: O(n), Space: O(1). Linear Scan.
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curLen, maxLen = 0, 0
        for n in nums:
            if n:
                curLen += 1
            else:
                curLen = 0
            maxLen = max(curLen, maxLen)
        return maxLen
