"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

 


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

 


The largest rectangle is shown in the shaded area, which has area = 10 unit.

 

Example:

Input: [2,1,5,6,2,3]
Output: 10
"""

# Time: O(n), Space: O(n).
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
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
