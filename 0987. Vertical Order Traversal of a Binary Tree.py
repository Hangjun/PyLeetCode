"""
Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

 

Example 1:



Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: 
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).
Example 2:



Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation: 
The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.
 

Note:

The tree will have between 1 and 1000 nodes.
Each node's value will be between 0 and 1000.
"""

# This problem is similar to Problem 314. The only difference is that now if two nodes are at the same width and depth, the tie 
# is broken by the value instead of left-to-right.
# BFS + Hash Table. Time: O(n), Space: O(n).
from collections import deque, defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return None
        minWidth, maxWidth = 0, 0
        ht = defaultdict(list)
        # (node, x, y)
        dq = deque([(root, 0, 0)])
        while dq:
            curLevelSize = len(dq)
            for _ in range(curLevelSize):
                node, x, y = dq.popleft()
                minWidth = min(minWidth, x)
                maxWidth = max(maxWidth, x)
                ht[x].append((node.val, y))
                if node.left:
                    dq.append((node.left, x-1, y+1))
                if node.right:
                    dq.append((node.right, x+1, y+1))
        
        res = []
        for x in range(minWidth, maxWidth+1):
            res.append([val for val, _ in sorted(ht[x], key=lambda x: (x[1], x[0]))])
        return res
