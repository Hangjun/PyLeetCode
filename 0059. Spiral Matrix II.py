"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

# Time: O(n^2), Space: O(n^2).
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for _ in range(n)] for _ in range(n)]
        u, d, l, r = 0, n-1, 0, n-1
        k = 1
        while True:
            # top row
            for col in range(l, r+1):
                res[u][col] = k
                k += 1
            u += 1
            if u > d:
                break
            
            # right col
            for row in range(u, d+1):
                res[row][r] = k
                k += 1
            r -= 1
            if r < l:
                break
            
            # bottom row
            for col in range(r, l-1, -1):
                res[d][col] = k
                k += 1
            d -= 1
            if d < u:
                break
            
            # left col
            for row in range(d, u-1, -1):
                res[row][l] = k
                k += 1
            l += 1
            if l > r:
                break
        return res
