"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""

# This problem is similar to https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/submissions/. 
# Morris traversal to find predecessor. Time: O(n), Space: O(1).
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        curNode = root
        while curNode:
            if curNode.left:
                prevNode = curNode.left
                while prevNode.right:
                    prevNode = prevNode.right
                prevNode.right = curNode.right
                curNode.right = curNode.left
                curNode.left = None # must zero out the left pointer
            curNode = curNode.right
        return root
