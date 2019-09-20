"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

# Typical Backtracking Algorithm.
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        if n == 0 or k == 0:
            return res
        self.combineDFS(1, n, k, [], res)
        return res
    
    def combineDFS(self, start, n, k, cur, res):
        # terminating condition
        if len(cur) == k:
            res.append(cur)
            return
        
        # backtracking
        for i in range(start, n+1):
            self.combineDFS(i+1, n, k, cur + [i], res)
