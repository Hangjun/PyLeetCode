"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""

# Binary Search. Time: O(logn), Space: O(1)
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right - left) / 2
            # if nums[mid: right] is sorted, then mid could be a candidate
            if nums[mid] < nums[right]:
                right = mid
            # if nums[left: mid] is sorted, then min must be in nums[mid+1: right]
            else:
                left = mid + 1
        return nums[left]
