"""
Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104
UPDATE (2017/9/19):
The arr parameter had been changed to an array of integers (instead of a list of integers). Please reload the code definition to get the latest changes.
"""

# Binary Search. Time: O(logn + k). Space: O(1)
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # Find the insertionn position
        pos = self.findInsertPos(arr, x)
        
        # pos divides the array into two parts, leftPart and rightPart. Merge sort the two parts
        left, right = pos-1, pos
        res = []
        count = 0
        while count < k:
            if left < 0:
                count += 1
                right += 1
            elif right >= len(arr):
                count += 1
                left -= 1
            else:
                if abs(arr[left] - x) <= abs(arr[right] - x):
                    count += 1
                    left -= 1
                else:
                    count += 1
                    right += 1
        
        # insert from left+1 to right-1
        for i in range(left+1, right):
            res.append(arr[i])
        return res
        
    def findInsertPos(self, arr, x):
        left, right = 1, len(arr) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        return left
