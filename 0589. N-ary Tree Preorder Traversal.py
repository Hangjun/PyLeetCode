"""
Given an n-ary tree, return the preorder traversal of its nodes' values.

For example, given a 3-ary tree:

Return its preorder traversal as: [1,3,5,6,2,4].

Note:

Recursive solution is trivial, could you do it iteratively?
"""

# We use the solution #2 of the preorder traversal of binary tree to generalize to this problem. Time: O(n), Space: O(n).
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            cur = stack.pop()
            if not cur:
                continue
            res.append(cur.val)
            stack.extend(cur.children[::-1])
        return res
