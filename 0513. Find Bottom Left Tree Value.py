"""
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.
"""

"""
Analysis: we are looking for a node with two properties: 1) it is leftmost, meaning that:
root.left and not root.left.left and not root.left.right.
Also 2) it is in the last row, meaning that it has the maximum depth.
Therefore during the DFS we need to keep track of both of these information. It is easy to keep track of the maximum depth. How 
do we keep track of whether it is a leftmost leaf? We can use the `root.left and not root.left.left and not root.left.right` check 
but a neat trick is, if we always start with the left child in the DFS, and only update the max depth reached if the current 
depth exceeds the max depth ever reached, we are guarratted to not record any leaf that is not leftmost since the leftmost node 
in the same depth must have already been explored.

DFS. Time: O(n), Space: O(1).
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.max_depth = 0
        self.dfs(root, 1)
        return self.res
    
    def dfs(self, cur_node, cur_depth):
        if not cur_node:
            return
        if cur_depth > self.max_depth:
            self.max_depth = cur_depth
            self.res = cur_node.val
        self.dfs(cur_node.left, cur_depth + 1)
        self.dfs(cur_node.right, cur_depth + 1)

"""
We can solve this problem using BFS. The idea is that, we level order traverse the tree from right to left, level by level. The 
node we are looking for is the LAST node in this traversal. This is very similar to https://leetcode.com/problems/binary-tree-right-side-view/.
"""
from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        dq = deque([root])
        while root and dq:
            cur_level_size = len(dq)
            for _ in range(cur_level_size):
                node = dq.popleft()
                res = node.val
                if node.right:
                    dq.append(node.right)
                if node.left:
                    dq.append(node.left)
        return res
