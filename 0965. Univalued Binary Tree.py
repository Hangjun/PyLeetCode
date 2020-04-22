"""
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.


Example 1:


Input: [1,1,1,1,1,null,1]
Output: true
Example 2:


Input: [2,2,2,5,2]
Output: false
"""

# DFS. Time: O(n), Space: O(logn)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        isLeftUnivalue = self.isUnivalTree(root.left)
        isRightUnivalue = self.isUnivalTree(root.right)
        if isLeftUnivalue and isRightUnivalue:
            if (not root.left or root.val == root.left.val) and (not root.right or root.val == root.right.val):
                return True
        return False
