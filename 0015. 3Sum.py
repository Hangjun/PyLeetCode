"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
# Time: O(n^2), Space: O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        n = len(nums)
        nums.sort()
        
        if n < 3:
            return res
 
        for i in range(n - 2):
            if nums[i] > 0:
                break
                
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            l,r = i + 1, n-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and  nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        
        return res

