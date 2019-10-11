"""
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

Example 1:

Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3

Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:

Input:

   2
    \
     3
    / 
   2    
  / 
 1

Output: 2 

Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
"""

# This problem is similar to https://leetcode.com/problems/longest-univalue-path/. DFS solution. Time: O(n), Space: O(1).
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.dfs(root)
        return self.res
    
    # invariant: compute the lenght of the longest consecutive sequence from root
    def dfs(self, root):
        if not root:
            return 0
        left_path = self.dfs(root.left)
        right_path = self.dfs(root.right)
        left = left_path + 1 if root.left and root.val + 1 == root.left.val else 1
        right = right_path + 1 if root.right and root.val + 1 == root.right.val else 1
        self.res = max(self.res, max(left, right))
        return max(left, right)
