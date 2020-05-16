"""
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2
 

return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
"""

"""
The idea is to inorder traverse the BST so that we get a non-decreasing list. We walk the list and compare the current value with 
the previous value to decide the longest same-value streak. Note that all the book-keeping variables are global, just imagine 
that we are traversing an array.

Time: O(n), Space: O(n) - recursive stack.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.prev = None
        self.modes = []
        self.curCount = 0
        self.maxCount = 0
        self.inorder(root)
        return self.modes
    
    # in order traverse the BST
    def inorder(self, curNode):
        if not curNode:
            return
        self.inorder(curNode.left)
        if curNode.val != self.prev:
            self.curCount = 1
        else:
            self.curCount += 1
        if self.curCount == self.maxCount:
            self.modes.append(curNode.val)
        elif self.curCount > self.maxCount:
            self.modes = [curNode.val]
            self.maxCount = self.curCount
        
        self.prev = curNode.val
        self.inorder(curNode.right)
