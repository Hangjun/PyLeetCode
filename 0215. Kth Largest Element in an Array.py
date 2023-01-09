"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

# quick select. Same solution. different way to code

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        l, r = 0, len(nums)-1
        
        def pivot(l, r):         
            n = nums[l]
            while l < r:
                if nums[l]>nums[l+1]:
                    nums[r], nums[l+1] = nums[l+1], nums[r]
                    r-=1
                elif nums[l]<nums[l+1]:
                    nums[l], nums[l+1] = nums[l+1], nums[l]
                    l+=1
                else:
                    l+=1
            return l
        
        while l<r:
            p = pivot(l,r)
            if p==k-1:
                return nums[p]
            elif p>k-1:
                r = p-1
            else:
                l = p+1
                
        return nums[l]
            
            





# Quick Select. Average Time: O(n), Worse Case Time: O(n^2). Space: O(1). 
# T(n) = T(n/2) + O(n) => T(n) = O(n) on average.
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while True:
            pos = self._partition(nums, left, right)
            if pos == k-1:
                return nums[pos]
            elif pos > k-1:
                right = pos-1
            else:
                left = pos+1
        
    def _partition(self, nums, left, right):
        pivot = nums[left]
        l, r = left+1, right
        while l <= r:
            if nums[l] < pivot and nums[r] > pivot:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            if nums[l] >= pivot:
                l += 1
            if nums[r] <= pivot:
                r -= 1
        # [>= pivot, pivot, <= pivot]
        nums[left], nums[r] = nums[r], nums[left]
        return r
