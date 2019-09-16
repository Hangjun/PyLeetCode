"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true
 

Note:

1 <= A.length <= 50000
-100000 <= A[i] <= 100000
"""

# Linear Scan. Time: O(n), Space: (1)
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        direction = None
        for i in range(len(A)-1):
            diff = A[i] - A[i+1]
            if diff == 0:
                continue
            diff = diff < 0
            if direction is None:
                direction = diff
            if direction != diff:
                return False
        return True

# A different divide-and-conquer solution.
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 2:
            return True
        left, right = 0, len(A)-1
        mid = left + (right - left) / 2
        if (A[left] - A[mid]) * (A[mid] - A[right]) < 0:
            return False
        return self.isMonotonic(A[left:mid+1]) and self.isMonotonic(A[mid: right+1])
