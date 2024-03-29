"""
(This problem is an interactive problem.)

A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [rows, cols], which means the matrix is rows * cols.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes you're given the binary matrix mat as input in the following four examples. You will not have access the binary matrix directly.

 

 

 

Example 1:



Input: mat = [[0,0],[1,1]]
Output: 0
Example 2:



Input: mat = [[0,0],[0,1]]
Output: 1
Example 3:



Input: mat = [[0,0],[0,0]]
Output: -1
Example 4:



Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
Output: 1
 

Constraints:

rows == mat.length
cols == mat[i].length
1 <= rows, cols <= 100
mat[i][j] is either 0 or 1.
mat[i] is sorted in a non-decreasing way.
"""

# Solution #1: Stepwise Binary Search. Time: O(m+n), Space: O(1).
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row, col):
#        """
#        :type row : int, col : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        m, n = binaryMatrix.dimensions()
        # going from top right to bottom left
        row, col = 0, n-1
        while row < m and col >= 0:
            curVal = binaryMatrix.get(row, col)
            if curVal:
                col -= 1
            else:
                row += 1
        return col + 1 if col != n-1 else -1
        
# Solution #2: Binary Search for each row to get the first index of 1. Time: O(mlogn), Space: O(1).
class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        m, n = binaryMatrix.dimensions()
        res = n
        # search each row to compute the index of the first 1, if exists
        for row in range(m):
            left, right = 0, n-1
            while left < right:
                mid = left + (right - left) / 2
                if binaryMatrix.get(row, mid):
                    right = mid
                else:
                    left = mid + 1
            if binaryMatrix.get(row, left):
                res = min(res, left)
        return res if res != n else -1
