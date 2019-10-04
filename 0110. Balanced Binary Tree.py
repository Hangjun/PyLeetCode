"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""

"""
Analysis: The brute-force solution is to compute the height at every node, and then traverse the tree again to see if the tree 
is balanced. A better approach is to perform a bottom-up DFS search such that each DFS search computes the height of the subtree 
rooted at the current node:

Time: O(n), Space: O(1).
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.res = True
        self.dfs(root)
        return self.res
    
    # invariant: compute the height of the subtree rooted at current node
    def dfs(self, root):
        if not root:
            return 0
        leftHeight = self.dfs(root.left)
        rightHeight = self.dfs(root.right)
        if abs(leftHeight - rightHeight) > 1:
            self.res = False
        return 1 + max(leftHeight, rightHeight)

"""
However, we could have stopped the DFS as soon as the tree is found to be imbalanced. The trick here is how to pass both the 
height information as well as the imbalancedness information upward. Learn this trick: we can use -1 as a sentinel. This way no 
computation will be wasted.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root) != -1
    
    # invariant: compute the height of the subtree rooted at current node
    def dfs(self, root):
        if not root:
            return 0
        leftHeight = self.dfs(root.left)
        if leftHeight == -1:
            return -1
        rightHeight = self.dfs(root.right)
        if rightHeight == -1:
            return -1
        return 1 + max(leftHeight, rightHeight) if abs(leftHeight - rightHeight) <= 1 else -1
