"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

 

Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10
 

Note: Your solution should run in O(log n) time and O(1) space.
"""

# Binary Search. The key obsevation is that this single number can only occur at an even index. We can think of the array as 
# consisting of n/2 pairs, among which one pair is fake as it only contains a single element. We binary search on the pair 
# indices. Starting with left = 0 and right = n/2, mid = left + (right-left)/2. Here left, mid and right are indices for the 
# pairs (again, one of the pairs is fake and has only one element). Imagine that if all pairs are real, then nums[2*ind] == nums[2*ind+1] 
# for any pair index ind. But since one pair is fake. we must have an index, within [left, right], such that the above equality 
# does NOT hold. The goal of the binary search to find this pair index.
# Suppose nums[2*mid] == nums[2*mid+1], then the index of the fake pair must lie within [mid+1, right]. This is because if was 
# in [left, mid], it would have messed up with all the pair after it. For the same reason, if nums[2*mid] != nums[2*mid+1], then 
# the fake pair's index must lie within [left, mid].

Time: O(logn), Space: O(1).
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # left and right are the index of the pairs in nums
        left, right = 0, len(nums)/2
        
        # find the first pair index m such that nums[2m] != nums[2m+1]
        while left < right:
            mid = left + (right-left)/2
            if nums[2*mid] != nums[2*mid+1]:
                right = mid
            else:
                left = mid+1
        return nums[2*left]
