"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

# Same de-dup logic. Backtracking DFS.
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.permuteDFS(nums, [], res)
        return res
    
    def permuteDFS(self, nums, cur, res):
        if not nums:
            res.append(cur)
            return
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.permuteDFS(nums[:i] + nums[i+1:], cur + [nums[i]], res)
