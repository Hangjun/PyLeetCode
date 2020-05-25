"""
Given a rooted binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children
The depth of the root of the tree is 0, and if the depth of a node is d, the depth of each of its children is d+1.
The lowest common ancestor of a set S of nodes is the node A with the largest depth such that every node in S is in the subtree with root A.
 

Example 1:

Input: root = [1,2,3]
Output: [1,2,3]
Explanation: 
The deepest leaves are the nodes with values 2 and 3.
The lowest common ancestor of these leaves is the node with value 1.
The answer returned is a TreeNode object (not an array) with serialization "[1,2,3]".
Example 2:

Input: root = [1,2,3,4]
Output: [4]
Example 3:

Input: root = [1,2,3,4,5]
Output: [2,4,5]
 

Constraints:

The given tree will have between 1 and 1000 nodes.
Each node of the tree will have a distinct value between 1 and 1000.
"""

# First we BFS to find the depths of each node. Then we find the LCA of the deepest node via recursion.
# Time: O(n), Space: O(n).
from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.ht = defaultdict(int)
        self.depth = self.findDepth(root)
        return self.findAnc(root)
    
    def findAnc(self, root):
        if not root: 
            return None
        if self.ht[root] == self.depth:
            return root
        l, r = self.findAnc(root.left), self.findAnc(root.right)
        if l and r:
            return root
        elif l:
            return l
        elif r:
            return r
        else:
            return None
    
    def findDepth(self, root):
        queue = deque([root])
        curDepth = 0
        while queue:
            curSize = len(queue)
            for _ in range(curSize):
                curNode = queue.popleft()
                self.ht[curNode] = curDepth
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
            curDepth += 1
        return curDepth-1
