"""
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.

 

Example 1:



Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
 

Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.
"""

# Recursion. Time: O(n), Space: O(n).
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        to_delete = set(to_delete)
        res = []
        
        # recursively process the children of the current node
        # recursively pass information downard regarding whether the current node is to be deleted or not
        def helper(curNode, is_root):
            if not curNode:
                return None
            need_to_delete = curNode.val in to_delete
            if is_root and not need_to_delete:
                res.append(curNode)
            curNode.left = helper(curNode.left, need_to_delete)
            curNode.right = helper(curNode.right, need_to_delete)
            return curNode if not need_to_delete else None
    
        helper(root, True)
        return res
