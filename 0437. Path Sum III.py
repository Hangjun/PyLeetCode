"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""

"""
DFS. Time: O(n^2), Space: O(1).

Since the path does not need to start from root, there are actually two variables in this problem: the starting node and the 
paths. It is difficult to deal with both in a single DFS. Fixing a starting node, we can use a DFS call to count all the paths 
eminating from this node. We can deligate the search at all the different starting node to another recursion.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        return self.countPathsDFS(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
    
    # Count the number of paths sum up to sum eminating from curNode
    def countPathsDFS(self, curNode, sum):
        if not curNode:
            return 0 # sum == 0 return result in double counting
        return (sum == curNode.val) + self.countPathsDFS(curNode.left, sum - curNode.val) + self.countPathsDFS(curNode.right, sum - curNode.val)
