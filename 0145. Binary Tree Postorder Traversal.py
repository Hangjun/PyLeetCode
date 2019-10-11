"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Two Stacks iterative solution. Time: O(n), Space: O(n).
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        pre_stack, ready_stack = [root], []
        while pre_stack:
            cur = pre_stack.pop()
            ready_stack.append(cur)
            if cur.left:
                pre_stack.append(cur.left)
            if cur.right:
                pre_stack.append(cur.right)
        
        while ready_stack:
            res.append(ready_stack.pop().val)
        return res
