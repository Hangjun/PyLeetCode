"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

# Time: O(mn), Space: O(mn).
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        u, d, l, r = 0, m-1, 0, n-1
        k = 0
        res = [0 for _ in range(m * n)]
        while True:
            # top row
            for col in range(l, r+1):
                res[k] = matrix[u][col]
                k += 1
            u += 1
            if u > d:
                break
            
            # right col
            for row in range(u, d+1):
                res[k] = matrix[row][r]
                k += 1
            r -= 1
            if r < l:
                break
            
            # bottom row
            for col in range(r, l-1, -1):
                res[k] = matrix[d][col]
                k += 1
            d -= 1
            if d < u:
                break
            
            # left col
            for row in range(d, u-1, -1):
                res[k] = matrix[row][l]
                k += 1
            l += 1
            if l > r:
                break
        return res
