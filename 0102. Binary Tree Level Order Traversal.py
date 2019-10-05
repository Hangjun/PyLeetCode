"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# BFS. Time: O(n), Space: O(n).
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res, level = [], [root]
        while root and level:
            res.append([node.val for node in level])
            level = [child for node in level for child in (node.left, node.right) if child]
        return res

# Another solution using queue:
from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res, level = [], deque([root])
        while root and level:
            curLevel, size = [], len(level)
            for _ in range(size):
                node = level.popleft()
                curLevel.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            res.append(curLevel)
            
        return res
