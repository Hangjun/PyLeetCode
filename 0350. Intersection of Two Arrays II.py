"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""

# One Hash Table. Time: O(m+n), Space: O(min(m,n))
from collections import defaultdict
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        freq = defaultdict(int)
        res = []
        for n in nums1:
            freq[n] += 1
        for m in nums2:
           if m in freq:
                freq[m] -= 1
                res.append(m)
                if freq[m] == 0:
                    freq.pop(m)
        return res

# Another solution is to use Python's built-in Counter data structure and the & operator:
from collections import defaultdict
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c1, c2 = map(collections.Counter, (nums1, nums2))
        return list((c1 & c2).elements())
