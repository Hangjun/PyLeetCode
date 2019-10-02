"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
"""

"""
This problem is very similar to https://leetcode.com/problems/path-sum-iv/. A generic pattern for tree DFS problems, when we are 
passing information downward, is:

# let curSoln := information being passed top down, e.g. path sum.
def dfs(self, curNode, curSoln):
  if not curNode:
    return 0 or None
  # now that curNode is not empty, compute the curSoln at this node:
  curSoln += curNode.val
  # if curNode is leaf node, return curSoln right away
  if not curNode.left and not curNode.right:
    return curSoln
  # otherwise DFS with both branches combined:
  return self.dfs(curNode.left, curSoln) + self.dfs(curNode.right, curSoln)
  
DFS solution. Time: O(n), Space: O(1).
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.dfs(root, 0)
    
    def dfs(self, curNode, curSum):
        if not curNode:
            return 0
        curSum = curSum * 10 + curNode.val
        if not curNode.left and not curNode.right:
            return curSum
        return self.dfs(curNode.left, curSum) + self.dfs(curNode.right, curSum)
