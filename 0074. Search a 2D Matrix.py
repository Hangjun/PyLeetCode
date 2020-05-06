"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""

# Solution #1: Stepwise Binary Search. Time: O(max(m, n)), Space: O(1).
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        if target < matrix[0][0] or target > matrix[m-1][n-1]:
            return False
        row, col = m-1, 0
        while row >= 0 and col < n:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row -= 1
            else:
                col += 1
        return False

# Solution #2: We perform a binary search in the virtual flattened vector. Time: O(log(mn)), Space: O(1).
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        if target < matrix[0][0] or target > matrix[m-1][n-1]:
            return False
        left = 0
        right = m * n - 1
        while left <= right:
            mid = left + (right - left) / 2
            if matrix[mid/n][mid%n] == target:
                return True
            elif matrix[mid/n][mid%n] < target:
                left += 1
            else:
                right -= 1
        return False
      
# Solution #3: Two Binary Searches. First identify the row, then search in the row. Time: O(log(m) + log(n)), Space: O(1).
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        # take care of out of bound
        if target < matrix[0][0] or target > matrix[m-1][n-1]:
            return False
        left, right = 0, m-1
        while left < right:
            mid = left + (right - left) / 2
            if matrix[mid][n-1] < target:
                left = mid + 1
            else:
                right = mid
        row = left
        left, right = 0, n-1
        while left <= right:
            mid = left + (right - left) / 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
