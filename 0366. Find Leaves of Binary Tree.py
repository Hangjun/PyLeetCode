"""
Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

 

Example:

Input: [1,2,3,4,5]
  
          1
         / \
        2   3
       / \     
      4   5    

Output: [[4,5,3],[2],[1]]
 

Explanation:

1. Removing the leaves [4,5,3] would result in this tree:

          1
         / 
        2          
 

2. Now removing the leaf [2] would result in this tree:

          1          
 

3. Now removing the leaf [1] would result in the empty tree:

          []         
"""

# We hash nodes according to their heights: height(node): length of the longest path to the leaf node in its subtree. The neat 
# thing is, after the DFS, the height_map is already sorted.
# Time: O(n), Space: O(n).

from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.height_map = defaultdict(list)
        self.findHeightDFS(root)
        # height_map is already sorted by keys
        res = []
        for i in range(len(self.height_map)):
            res.append(self.height_map[i])
        return res
        
    def findHeightDFS(self, root):
        if not root:
            return -1 # leaf nodes are height 0
        left_height = self.findHeightDFS(root.left)
        right_height = self.findHeightDFS(root.right)
        cur_height = 1 + max(left_height, right_height)
        self.height_map[cur_height].append(root.val)
        return cur_height
        
# We can also construct the height map using list. It is a bit tricky but very neat:
# Time: O(n), Space: O(n).
from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.res = []
        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        if not root:
            return -1 # leaf nodes are at height 0
        left_height = self.dfs(root.left)
        right_height = self.dfs(root.right)
        cur_height = 1 + max(left_height, right_height)
        if cur_height >= len(self.res): # new height found!
            self.res.append([])
        self.res[cur_height].append(root.val)
        return cur_height
