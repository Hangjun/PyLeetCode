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
# Time O(n!), Space(n)

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans = []
        self.dfs(1, n+1, k, [], ans)
        return ans
    
    def dfs(self,start, n, k, cur, ans):
        
        if k == 0:
            ans.append(cur)
            return
        
        for i in range(start, n):
            self.dfs(i+1, n, k-1, cur+[i], ans)
        
            
