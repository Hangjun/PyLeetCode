"""
Given a binary tree where every node has a unique value, and a target key k, find the value of the nearest leaf node to target k in the tree.

Here, nearest to a leaf means the least number of edges travelled on the binary tree to reach any leaf of the tree. Also, a node is called a leaf if it has no children.

In the following examples, the input tree is represented in flattened form row by row. The actual root tree given will be a TreeNode object.

Example 1:

Input:
root = [1, 3, 2], k = 1
Diagram of binary tree:
          1
         / \
        3   2

Output: 2 (or 3)

Explanation: Either 2 or 3 is the nearest leaf node to the target of 1.
Example 2:

Input:
root = [1], k = 1
Output: 1

Explanation: The nearest leaf node is the root node itself.
Example 3:

Input:
root = [1,2,3,4,null,null,null,5,null,6], k = 2
Diagram of binary tree:
             1
            / \
           2   3
          /
         4
        /
       5
      /
     6

Output: 3
Explanation: The leaf node with value 3 (and not the leaf node with value 6) is nearest to the node with value 2.
Note:
root represents a binary tree with at least 1 node and at most 1000 nodes.
Every node has a unique node.val in range [1, 1000].
There exists some node in the given binary tree for which node.val == k.
"""

# Convert to graph and BFS. The caveats are: if k is already a leaf node, return it directly. 
# Time: O(n), Space: O(n).
from collections import defaultdict, deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # step 1: construct adjList representation of the binary tree
        adj = defaultdict(list)
        self.dfs(root, None, adj)
        
        # corner cases
        if not adj or (len(adj[k]) == 1 and k != root.val):
            return k
        
        # step 2: BFS + visited to find the nearest leaf (no edge except with its parent)
        queue = deque([k])
        visited = set()
        visited.add(k)
        while queue:
            curSize = len(queue)
            for _ in range(curSize):
                curNode = queue.popleft()
                leafNode = True
                # if all neighbors of curNode has been visited, then curNode is a leaf node
                for nn in adj[curNode]:
                    if nn not in visited:
                        visited.add(nn)
                        queue.append(nn)
                        leafNode = False # curNode is not a leaf node
                if leafNode and curNode != root.val:
                    return curNode
                
    # invariant: construct root -> [parent, leftChild, rightChild] adjacency list
    def dfs(self, root, parent, adj):
        if not root:
            return
        if parent:
            adj[root.val].append(parent.val)
        if root.left:
            adj[root.val].append(root.left.val)
        if root.right:
            adj[root.val].append(root.right.val)
        self.dfs(root.left, root, adj)
        self.dfs(root.right, root, adj)
