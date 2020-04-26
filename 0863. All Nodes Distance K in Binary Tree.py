"""
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
 

Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
"""

# Typical graph + BFS problem. We first build the adjacency list representation of the tree and then perform BFS to find the 
# nodes.
# Graph + BFS. Time: O(n), Space: O(n).
from collections import defaultdict, deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        adjList = defaultdict(list)
        self.buildGraph(root, None, adjList)
        
        # BFS on the target node to retrieve the Kth level neighbors
        queue = deque([target])
        visited = set()
        visited.add(target)
        curDistance = 0
        res = []
        while queue:
            curSize = len(queue)
            # check terminating condition
            if curDistance == K:
                for _ in range(curSize):
                    res.append(queue.popleft().val)
                return res
            
            # BFS on the neighbors
            for _ in range(curSize):
                curNode = queue.popleft()
                for neighbor in adjList[curNode]:
                    # neighbor could be None if curNode is root
                    if neighbor and neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
            curDistance += 1
        return res
                    
    # Build the adjacency list representation of the tree
    def buildGraph(self, root, parent, adjList):
        if not root:
            return
        adjList[root].append(parent)
        if root.left:
            adjList[root].append(root.left)
        if root.right:
            adjList[root].append(root.right)
        self.buildGraph(root.left, root, adjList)
        self.buildGraph(root.right, root, adjList)
