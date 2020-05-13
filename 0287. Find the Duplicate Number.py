"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""

"""
This problem also has a very interesting solution using binary search. One natural idea is to binary search the given array to find the 
duplicate. After some thought we see that this is not possible, since if the duplicating number are in two seperate subarrays in the first 
place, then we would never be able to find it. The key giveaway is the 4th requirement given above: "There is only one duplicate number in 
the array, but it could be repeated more than once." This suggests that we should perform binary search on the RANGE [1,n]. 
We repeatedly divide the possible range [1,n] into two pieces: [left, mid] and [mid+1, right]. The key observation is that, if there are no 
duplicate, then there should be exactly mid - left + 1 many elements within the first range, and right-mid many element in the second range. 
Thus if there are more elements than desired, we know that there is a duplicate in that range. It is the range that we subdividing!

Time: O(nlogn), Space: O(1).
"""
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 1, len(nums)
        # binary search in the value range [left, right]
        while left < right:
            mid = left + (right - left) / 2
            if len([n for n in nums if left <= n <= mid]) > mid-left+1:
                right = mid
            else:
                left = mid+1
        return left
