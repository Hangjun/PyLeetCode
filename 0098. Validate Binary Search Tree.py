"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""

# Recursive Solution. Testing BST condition at every node.
# Time: O(logn), Space: O(1).
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if not self.isValidBST(root.left) or not self.isValidBST(root.right):
            return False
        if root.left:
            prev = root.left
            while prev.right:
                prev = prev.right
            if prev.val >= root.val:
                return False
        if root.right:
            next = root.right
            while next.left:
                next = next.left
            if next.val <= root.val:
                return False
        return True
