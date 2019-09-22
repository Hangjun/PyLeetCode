"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

# Time: O(n), Space: O(1).
# A good explanation on the algorithm: https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        i = j = len(nums)-1
        # find the longest non-increasing suffix
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1  
        # nums is reverse sorted
        if i == 0:
            return nums.reverse()
        k = i-1
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        
        # reverse nums[k+1:]
        l, r = k+1, len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
