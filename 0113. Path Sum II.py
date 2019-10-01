"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""

# DFS Solution. Time: O(n), Space: O(1).
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        self.dfs(root, sum, [], res)
        return res
    
    def dfs(self, root, sum, path, res):
        # terminate condition check at leaf nodee
        if not root.left and not root.right:
            if root.val == sum:
                res.append(path + [root.val])
                return
        # dfs on its children
        if root.left:
            self.dfs(root.left, sum - root.val, path + [root.val], res)
        if root.right:
            self.dfs(root.right, sum - root.val, path + [root.val], res)
