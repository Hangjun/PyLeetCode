"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        if n <= 0:
            return res
        self.combinationDFS(1, 9, k, n, [], res)
        return res
    
    def combinationDFS(self, start, end, k, target, cur, res):
        # terminating condition
        if target == 0 and len(cur) == k:
            res.append(cur)
            return
        
        # backtracking
        for i in range(start, end+1):
            if i > target:
                continue
            self.combinationDFS(i+1, end, k, target - i, cur + [i], res)
