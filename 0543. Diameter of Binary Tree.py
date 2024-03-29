"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""

"""
This problem is very similar to https://leetcode.com/problems/binary-tree-maximum-path-sum/. Whenever we compute the path that 
does not need to start at root or end at leaf, or even going through the root, we follow this DFS structure. The key is that, 
for each DFS call, the return value should be the a choice of either the left path or the right path.

DFS. Time: O(n), Space: O(1).
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        if not root:
            return 0
        left_depth = self.dfs(root.left)
        right_depth = self.dfs(root.right)
        self.res = max(self.res, left_depth + right_depth)
        return 1 + max(left_depth, right_depth)
