"""
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples 1:

Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]
Examples 2:

Input: [3,9,8,4,0,1,7]

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7 

Output:

[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Examples 3:

Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2

Output:

[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]
"""

# BFS. Time: O(nlogn), Space: O(n).
from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return None
        cols = defaultdict(list)
        queue = [(root, 0)]
        for node, i in queue:
            cols[i].append(node.val)
            if node.left:
                queue.append((node.left, i-1))
            if node.right:
                queue.append((node.right, i+1))

        return [cols[i] for i in sorted(cols)]

# We can improve the time complexity to O(n) by computing the min/max width (i.e. the vertical orders) while doing the BFS.
import collections
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return None
        minWidth, maxWidth = 0, 0
        cols = collections.defaultdict(list)
        queue = [(root, 0)]
        for node, i in queue:
            cols[i].append(node.val)
            minWidth = min(minWidth, i)
            maxWidth = max(maxWidth, i)
            if node.left:
                queue.append((node.left, i-1))
                print "enqueue ", node.left.val
            if node.right:
                queue.append((node.right, i+1))
                print "enqueue ", node.right.val
        return [cols[i] for i in range(minWidth, maxWidth+1) if i in cols]
