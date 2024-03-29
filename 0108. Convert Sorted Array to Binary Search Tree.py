"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""

# Recursion. Time: O(n), Space: O(logn).
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        return self.buildBST(nums, 0, len(nums)-1)
    
    def buildBST(self, nums, start, end):
        if start > end:
            return None
        rootInd = start + (end - start) / 2
        root = TreeNode(nums[rootInd])
        root.left = self.buildBST(nums, start, rootInd-1)
        root.right = self.buildBST(nums, rootInd+1, end)
        
        return root
