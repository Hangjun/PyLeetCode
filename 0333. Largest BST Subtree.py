"""
Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.

Example:

Input: [10,5,15,1,8,null,7]

   10 
   / \ 
  5  15 
 / \   \ 
1   8   7

Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one.
             The return value is the subtree's size, which is 3.
Follow up:
Can you figure out ways to solve it with O(n) time complexity?
"""

"""
Typical bottom-up DFS in binary trees. The tricky part here is to use float('inf') and float('-inf') to correctly handle invalid 
return values so they do not mess up the information flow upward. Similar to Problem 1026	Maximum Difference Between Node and Ancestor.

Time: O(n), Space: O(n).
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.dfs(root)
        return self.res
    
    # return min val, max val and size of this substree as a BST
    # if the subtree is not a BST, the size is -inf
    def dfs(self, root):
        if not root:
            return float('inf'), float('-inf'), 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        # valid BST
        if left[1] < root.val < right[0]:
            n = left[2] + right[2] + 1
        else:
            n = float('-inf')

        self.res = max(self.res, n, left[2], right[2])
        return min(root.val, left[0]), max(root.val, right[1]), n
