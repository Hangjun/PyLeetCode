"""
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

Example :

Input:  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

Output: 4
"""

"""
Similar to https://leetcode.com/problems/longest-univalue-path/.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.dfs(root)
        return self.res
    
    # invariant: is the subtree rooted at current node univalue
    def dfs(self, root):
        if not root:
            return True
        isLeftUnivalue = self.dfs(root.left)
        isRightUnivalue = self.dfs(root.right)
        if isLeftUnivalue and isRightUnivalue:
            if (not root.left or root.val == root.left.val) and (not root.right or root.val == root.right.val):
                self.res += 1
                return True
        return False
