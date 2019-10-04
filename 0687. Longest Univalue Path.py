"""
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output: 2

 

Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output: 2

Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
"""

"""
This problem is very similar to https://leetcode.com/problems/diameter-of-binary-tree/. Same structure.
DFS. Time: O(n), Space: O(1).
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.dfs(root)
        return self.res
    
    # invariant: compute the length of the longer univalue path passing through current node
    def dfs(self, root):
        if not root:
            return 0
        left_path = self.dfs(root.left)
        right_path = self.dfs(root.right)
        left = left_path + 1 if root.left and root.left.val == root.val else 0
        right = right_path + 1 if root.right and root.right.val == root.val else 0
        self.res = max(self.res, left + right)
        return max(left, right)
