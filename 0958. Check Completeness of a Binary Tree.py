"""
Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

 

Example 1:



Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
Example 2:



Input: [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
 
Note:

The tree will have between 1 and 100 nodes.
"""

"""
We perform level order traversal while keeping track of the indices of each node. We store all the levels then we perform a 
second scan to check for the completeness.

Time: O(n), Space: O(n).
"""
from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        levels = []
        dq = deque([(root, 0)])
        while dq:
            curLevel = []
            for _ in range(len(dq)):
                node, i = dq.popleft()
                curLevel.append((node, i))
                if node.left:
                    dq.append((node.left, 2*i))
                if node.right:
                    dq.append((node.right, 2*i+1))
            levels.append(curLevel)
        
        n = len(levels)
        for i in range(n):
            if i < n-1 and len(levels[i]) != pow(2, i):
                return False
            if i == n-1:
                for j in range(0, len(levels[i])):
                    if j == 0 and levels[i][j][1]:
                        return False
                    if j >= 1 and levels[i][j][1] != levels[i][j-1][1] + 1:
                        return False
                    
        return True
        
"""
We can improve the above solution to check for completeness WHILE performing the level order traversal. The trick here is, the 
indices computation using 2*i and 2*i+1 will always be starting from 0 for each new level. If we want to have a continous count 
of the node with respect to the entire binary tree, we can use 2*i+1 and 2*i+2. This is a reallly neat trick.

Time: O(n), Space: O(n).
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        queue = [(root, 0)]
        count = 0
        for node, i in queue:
            count += 1
            if count - 1 != i:
                return False
            if node.left:
                queue.append((node.left, 2*i+1))
            if node.right:
                queue.append((node.right, 2*i+2))
        return True
