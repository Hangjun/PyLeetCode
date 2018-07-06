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
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if (len(nums) < 3): return []
        
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]): # except the last two elements
            # de-duplicate
            if i > 0 and v == nums[i-1]: continue
            left, right = i+1, len(nums)-1
            while left < right:
                tmpSum = v + nums[left] + nums[right]
                if tmpSum == 0:
                    res.add((v, nums[left], nums[right]))
                    left += 1
                    right -= 1
                    # de-duplicate
                    while left < right and nums[left] == nums[left-1]: left += 1
                    while left < right and nums[right] == nums[right+1]: right -= 1
                elif tmpSum < 0:
                    left += 1
                else:
                    right -= 1
        
        return map(list, res)
                    
"""
Remark：
1. 我们当然可以把这个问题拆解为一个2Sum外面套一个for loop，但是这并不是最优解，因为2Sum还需要一个dictionary占用多余的空间复杂度。
2. 上面由于我们用了Python的set，其实会自动帮我们去重（假如我没有理解错Python set的定义的话）。但是我们要尽可能的少依赖自带的数据结构的优势，而是从
算法上更加严谨的implement。
"""
    
