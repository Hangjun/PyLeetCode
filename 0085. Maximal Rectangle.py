"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
"""

# Time: O(n^2), Space: O(n).
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        heightMap = [0 for _ in range(n)]
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    heightMap[j] += 1
                else:
                    heightMap[j] = 0
            # calculate largest rectangle after each row
            res = max(res, self.largestRectangle(heightMap))
        
        return res
    
    def largestRectangle(self, heights):
        maxArea = 0
        stack = [-1]
        for i, h in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] >= h:
                t = stack.pop()
                maxArea = max(maxArea, heights[t]*(i-stack[-1]-1))
            stack.append(i)
        
        lastIndex = stack[-1]
        while stack[-1] != -1:
            t = stack.pop()
            maxArea = max(maxArea, heights[t]*(lastIndex-stack[-1]))
        
        return maxArea
