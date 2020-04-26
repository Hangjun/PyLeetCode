"""
Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:

Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:

Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
Example 3:

Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
Example 4:

Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


Note: Answer will in the range of 32-bit signed integer.
"""

"""
On the first thought, we simply perform a level order traversal and record the width of each level. To compute the width, it is 
attempting to use the same width computation as in Vertical Order Traversal. However, this is not how width is defined in this 
problem. In the Vertical Order Traversal problem, two nodes can have the same width. But here, each node occupies a unique width 
within the same level. What this problem is really asking is to comptue the _index_ of the nodes at each level and compute the maximum 
span of indices. Suppose a node is the ith node at level j, then its children will occupy the 2i and 2i+1's position in level j+1.

Level order traversal. Time: O(n), Space: O(n).
"""
from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = 1
        dq = deque([(root, 0)])
        left = right = 0
        while dq:
            # get the current level
            curLevelSize = len(dq)
            for i in range(curLevelSize):
                curNode, curInd = dq.popleft()
                if i == 0:
                    left = curInd
                if i == curLevelSize - 1:
                    right = curInd
                if curNode.left:
                    dq.append((curNode.left, 2 * curInd))
                if curNode.right:
                    dq.append((curNode.right, 2 * curInd + 1))
            # compute the width of current level and update res
            res = max(res, right-left+1)
        return res
