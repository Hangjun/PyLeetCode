"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""

# DFS solution. Time: O(n), Space: O(1).
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.max_depth = 0
        self.dfs(root, 1, res)
        return res
    
    def dfs(self, cur_node, cur_depth, res):
        if not cur_node:
            return
        if cur_depth > self.max_depth:
            self.max_depth = cur_depth
            res.append(cur_node.val)
        self.dfs(cur_node.right, cur_depth + 1, res)
        self.dfs(cur_node.left, cur_depth + 1, res)

# BFS solution. Level order traversal. Time: O(n), Space: O(n).
from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        level = [root]
        while root and level:
            res.append(level[-1].val)
            level = [child for node in level for child in (node.left, node.right) if child]
        return res
