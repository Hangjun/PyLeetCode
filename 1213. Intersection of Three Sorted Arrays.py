"""
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

 

Example 1:

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.
 

Constraints:

1 <= arr1.length, arr2.length, arr3.length <= 1000
1 <= arr1[i], arr2[i], arr3[i] <= 2000
"""

# Hash table. Depends on the given assumption that all arrays are strictly increasing. 
# Time: O(nlogn), Space: O(n). n = average len of each array.
from collections import defaultdict
class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        freq = defaultdict(int)
        for n in arr1 + arr2 + arr3:
            freq[n] += 1
        return sorted([num for num, count in freq.items() if count == 3])

# However, the above algorithm does not make use of the fact that the input arrays are already sorted. Here is a better algorithm 
# using three pointers and takes O(n) time, O(1) space.
# Three Pointers. Time: O(n), Space: O(1).
class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        p1, p2, p3 = 0, 0, 0
        res = []
        while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
            v1, v2, v3 = arr1[p1], arr2[p2], arr3[p3]
            minVal = min(v1, v2, v3)
            if v1 == v2 and v2 == v3:
                res.append(v1)
            if v1 == minVal:
                p1 += 1
            if v2 == minVal:
                p2 += 1
            if v3 == minVal:
                p3 += 1
        return res

