"""
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

 
Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

 
Note: 

1 <= preorder.length <= 100
The values of preorder are distinct.
"""

# Sort. Time: O(nlogn), Space: O(n) for storing the inorder traversal.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        inorder = sorted(preorder)
        return self.buildTree(preorder, inorder)
    
    def buildTree(self, preorder, inorder):
        if not inorder:
            return None
        root_ind = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[root_ind])
        root.left = self.buildTree(preorder, inorder[:root_ind])
        root.right = self.buildTree(preorder, inorder[root_ind+1:])
        return root

"""
We can utilize the BST structure to improve the time complexity. The key is that, for a BST, once we identify the root, we can 
recursively build the left subtree by using root.val as the upper bound, and inf as the upper bound for the right subtree.
Time: O(n), Space: O(1).
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        self.preInd = 0
        return self.helper(preorder)
    
    def helper(self, preorder, bound = float('inf')):
        if self.preInd == len(preorder) or preorder[self.preInd] > bound:
            return None
        node = TreeNode(preorder[self.preInd])
        self.preInd += 1
        node.left = self.helper(preorder, node.val)
        node.right = self.helper(preorder, bound)
        return node
