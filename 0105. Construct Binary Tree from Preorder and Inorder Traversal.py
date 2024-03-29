"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

# Recursive solution. Caution that need to check emptiness of inorder list during the traversal.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder: 
            return None
        root_ind = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[root_ind])
        root.left = self.buildTree(preorder, inorder[0:root_ind])
        root.right = self.buildTree(preorder, inorder[root_ind + 1:])
        return root
