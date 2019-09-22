"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

# Backtracking DFS.
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res
    
    def dfs(self, nums, start, path, res):
        res.append(path)
        for i in range(start, len(nums)):
            if i > start and nums[i-1] == nums[i]:
                continue
            self.dfs(nums, i+1, path + [nums[i]], res)

# Solution #2: Iterative Solution. We can still use an interative solution to construct the result set. We just need to check 
# for duplicates, which is an expensive operation:
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for n in sorted(nums):
            res += [pre + [n] for pre in res if pre + [n] not in res]
        return res
