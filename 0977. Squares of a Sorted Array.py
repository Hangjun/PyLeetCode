"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

 

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
"""

# Binary Search + Merge Sort. Time: O(n), Space: O(1).
class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # binary search to find the first positive number's index
        left, right = 0, len(A)-1
        
        # loop invariant: first positive lives in [left, right]
        while left < right:
            mid = left + (right-left)/2
            if A[mid] < 0:
                left = mid + 1
            else:
                right = mid
        # merge sort A[:right] and A[right:] into res
        res = []
        neg, pos = right-1, right
        while neg >= 0 or pos < len(A):
            if neg >= 0 and pos < len(A):
                if abs(A[neg]) < abs(A[pos]):
                    res.append(A[neg] ** 2)
                    neg -= 1
                else:
                    res.append(A[pos] ** 2)
                    pos += 1
            elif neg >= 0:
                while neg >= 0:
                    res.append(A[neg] ** 2)
                    neg -= 1
            else:
                while pos < len(A):
                    res.append(A[pos] ** 2)
                    pos += 1
        return res
