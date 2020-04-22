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

Time: O(n), Space: O(logn) - for the recursive call stack. Single DFS.
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
            return self.res
        # global variable associated with the class
        self.res = root.val
        self.dfs(root)
        return self.res
    
    # Returns the maxium path sum either starting from root or ending at root
    def dfs(self, root):
        if not root:
            return 0
        left_path_sum = self.dfs(root.left)
        right_path_sum = self.dfs(root.right)
        self.res = max(self.res, left_path_sum + right_path_sum + root.val)
        # Choose either left path, or right path, or an empty path
        return max(root.val + max(left_path_sum, right_path_sum), 0)

# As a follow up, we can printn out the actual path with the maximum sum. The idea is the same: each dfs returns the one-sided 
# maximum path, each node, after its left dfs call and right dfs call, assembles the global max sum path and update a global 
# variable.
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
            return self.res
        # global variable associated with the class
        self.res = root.val
        self.max_path = []
        self.dfs(root)
        print('final... max_path = ', self.max_path)
        return self.res
    
    # Returns the maxium path sum either starting from root or ending at root
    def dfs(self, root):
        if not root:
            return 0, []
        left_path_sum, left_path = self.dfs(root.left)
        right_path_sum, right_path = self.dfs(root.right)
        cur_max_path_sum = left_path_sum + right_path_sum + root.val
        if cur_max_path_sum > self.res:
            self.res = cur_max_path_sum
            self.max_path = left_path + [root.val] + right_path
        # Choose either left path, or right path, or an empty path
        max_path_sum = max(root.val + max(left_path_sum, right_path_sum), 0)
        max_path = []
        if max_path_sum > 0:
            if left_path_sum > right_path_sum:
                max_path = left_path + [root.val]
            else:
                max_path = [root.val] + right_path
        return max_path_sum, max_path
