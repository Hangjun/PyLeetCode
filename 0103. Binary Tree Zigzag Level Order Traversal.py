"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

# BFS. Time: O(n), Space: (n)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res, level = [], [root]
        count = 0
        while root and level:
            curLevel = [node.val for node in level]            
            if count % 2 == 0:
                res.append(curLevel)
            else:
                res.append(curLevel[::-1])
            count += 1
            level = [child for node in level for child in (node.left, node.right) if child]
        return res
