"""
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""

# Time: O((logn)^2), Space: O(1).
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        leftHeight = rightHeight = 0
        leftNode = rightNode = root
        while leftNode:
            leftHeight += 1
            leftNode = leftNode.left
        while rightNode:
            rightHeight += 1
            rightNode = rightNode.right
        if leftHeight == rightHeight:
            return pow(2, leftHeight)-1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
