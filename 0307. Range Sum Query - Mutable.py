"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
"""

# Segment Tree. Time: O(n) to build the segment tree, O(logn) for each update/search query. Total time: O(n). Space: O(n).
class segmentTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.root = self._createSegmentTree(nums, 0, len(nums)-1)
        
    def _createSegmentTree(self, nums, l, r):
        if l > r:
            return None
        
        # base case: leaf node
        if l == r:
            node = segmentTreeNode(l, r)
            node.total = nums[l]
            return node
        
        root = segmentTreeNode(l,r)
        mid = l + (r - l) / 2
        root.left = self._createSegmentTree(nums, l, mid)
        root.right = self._createSegmentTree(nums, mid+1, r)
        root.total = root.left.total + root.right.total
        
        return root
        
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        self._updateNodeVal(self.root, i, val)
        
    # find the node in the segment tree and propogate the value update upward
    def _updateNodeVal(self, curNode, i, val):
        if curNode.start == curNode.end:
            assert(curNode.start == i)
            curNode.total = val
            return val
        mid = curNode.start + (curNode.end - curNode.start) / 2
        if i <= mid:
            self._updateNodeVal(curNode.left, i, val)
        else:
            self._updateNodeVal(curNode.right, i, val)

        curNode.total = curNode.left.total + curNode.right.total
        return curNode.total
        
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._sumRangeHelper(self.root, i, j)
    
    def _sumRangeHelper(self, curNode, i, j):
        if curNode.start == i and curNode.end == j:
            return curNode.total
        mid = curNode.start + (curNode.end - curNode.start) / 2
        if j <= mid:
            return self._sumRangeHelper(curNode.left, i, j)
        elif i > mid:
            return self._sumRangeHelper(curNode.right, i, j)
        else:
            return self._sumRangeHelper(curNode.left, i, mid) + self._sumRangeHelper(curNode.right, mid+1, j)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
