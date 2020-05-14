"""
Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)

 

Example 1:



Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: 
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
 

Note:

The number of nodes in the tree is between 2 and 5000.
Each node will have value between 0 and 100000.
"""

# Bottom-Up DFS. The tricky part is how to handle return values for leaf nodes.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.res = 0
        self.dfs(root)
        return self.res
    
    # return the max and min of the descents of the subtree rooted at root
    def dfs(self, root):
        if not root:
            return float('inf'), float('-inf')
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        childMin = min(left[0], right[0])
        childMax = max(left[1], right[1])
        
        diffWithMin = abs(root.val - childMin)
        diffWithMax = abs(root.val - childMax)
        if diffWithMin != float('inf') and diffWithMin > self.res:
            self.res = diffWithMin
        if diffWithMax != float('inf') and diffWithMax > self.res:
            self.res = diffWithMax
        
        return min(root.val, childMin), max(root.val, childMax)
