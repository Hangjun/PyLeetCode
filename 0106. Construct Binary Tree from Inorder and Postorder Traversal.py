"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

# Recursive solution. Worst case running time: O(n^2), Space: O(1). Notice that the order or the subtree construction needs to be right first, left second.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        root_ind = inorder.index(postorder.pop())
        root = TreeNode(inorder[root_ind])
        root.right = self.buildTree(inorder[root_ind+1:], postorder)
        root.left = self.buildTree(inorder[0:root_ind], postorder)
        return root
