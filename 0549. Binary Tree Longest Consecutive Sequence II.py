"""
Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:

Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
 

Example 2:

Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
 

Note: All the values of tree nodes are in the range of [-1e7, 1e7].
"""

"""
This problem is a generalization of https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/. This time two things 
are relaxed: 1. the path can be going from any node to any node; 2. the path can be either increasing or decreasing. We can 
take the approach of computing the longest uni-value path and compute, on each DFS, the longest path eminating from the current 
node while updating a global res. That implementation can be rather messy. Instead, we take a new approach and compute two 
things during each DFS: the maximum increase value and the maximum decrease value from both sides.

Time: O(n), Space: O(n).
"""
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
    
    def dfs(self, root):
        if not root:
            return 0, 0
        # inc and dec counts the number of increasing and decreasing consecutive nodes from root
        # both inc and dec paths are one-sided
        inc, dec = 1, 1
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if root.left:
            if root.left.val - 1 == root.val:
                inc = max(inc, left[0] + 1)
            elif root.left.val + 1 == root.val:
                dec = max(dec, left[1] + 1)
        if root.right:
            if root.right.val - 1 == root.val:
                inc = max(inc, right[0] + 1)
            elif root.right.val + 1 == root.val:
                dec = max(dec, right[1] + 1)
        self.res = max(self.res, inc + dec - 1)
        return inc, dec

