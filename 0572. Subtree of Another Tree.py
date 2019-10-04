"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""

# The brute-force solution is trivial:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return False
        return self.isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def isSameTree(self, s, t):
        return s and t and s.val == t.val and all(map(self.isSameTree, (s.left, s.right), (t.left, t.right))) or s is t

# We can serialize both trees (e.g. via pre-order traversal) and check whether t_serialize is a substring in s_serialize using KMP.
# Time: O(m+n), Space: O(m+n). Assuming the Python implementation of t in s runs in O(m+n) time.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def serialize(s):
            return "^" + str(s.val) + "#" + serialize(s.left) + serialize(s.right) if s else "$"
        return serialize(t) in serialize(s)
