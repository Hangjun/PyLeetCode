"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

# Solution #1: Iterative Construction. Since we know what the final results would look like, we can construct it iteratively.
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for n in nums:
            res += [pre + [n] for pre in res]
        return res

# Solution #2. Backtracking DFS.
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.subsetsDFS(nums, 0, [], res)
        return res
    
    def subsetsDFS(self, nums, start, path, res):
        res.append(path)
        for i in range(start, len(nums)):
            self.subsetsDFS(nums, i+1, path + [nums[i]], res)
