"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""

"""
This problem is similar to https://leetcode.com/problems/path-sum-iii/. There are multiple variables: the path does not need to 
start at root and end at leaf, it also does not need to go from top to bottom. The idea is, during the DFS we always return the 
optimal path sum EITHER starting at the current node going to the right, OR ending at the current node coming from the left. The 
reason being that, the caller of this DFS has to pick one of the two paths, if the current node gets selected. At the same time, 
we use a global variable to track the optimal path sum so far.

One caveat is, the global res needs to be initialized to be root.val since the problem requires the path to have at least one node.

Time: O(n), Space: O(1). Single DFS.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.res = root.val
        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        if not root:
            return 0
        left_path = self.dfs(root.left)
        right_path = self.dfs(root.right)
        self.res = max(self.res, max(left_path, 0) + max(right_path, 0) + root.val)
        return max(max(left_path, right_path), 0) + root.val
