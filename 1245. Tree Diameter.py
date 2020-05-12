"""
Given an undirected tree, return its diameter: the number of edges in a longest path in that tree.

The tree is given as an array of edges where edges[i] = [u, v] is a bidirectional edge between nodes u and v.  Each node has labels in the set {0, 1, ..., edges.length}.

 

Example 1:



Input: edges = [[0,1],[0,2]]
Output: 2
Explanation: 
A longest path of the tree is the path 1 - 0 - 2.
Example 2:



Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
Output: 4
Explanation: 
A longest path of the tree is the path 3 - 2 - 1 - 4 - 5.
 

Constraints:

0 <= edges.length < 10^4
edges[i][0] != edges[i][1]
0 <= edges[i][j] <= edges.length
The given edges form an undirected tree.
"""

"""
This is a generalization of Problem 543. Diameter of Binary Tree. Here the tree structure is not given explicitly. We treat it 
as a undirected graph without cycles. The idea is the same DFS. On each DFS, we return the length of the one-sided path passing 
through current node, at the same time, we update the global result by fetching the two longest child paths. Since we no longer 
have a binary tree, we need to traverse all the children and manually keep track of the top two lengths.

Time: O(n), Space: O(1).
"""
from collections import defaultdict
class Solution(object):
    def treeDiameter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        # build adjacency list
        adjList = defaultdict(list)
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        self.res = 0
        self.dfs(0, -1, adjList)
        return self.res
    
    def dfs(self, root, parent, adjList):
        firstMax, secondMax = 0, 0
        for child in adjList[root]:
            # manually control no backtrack
            if child == parent:
                continue
            childRes = self.dfs(child, root, adjList)
            if childRes > firstMax:
                secondMax = firstMax
                firstMax = childRes
            elif childRes > secondMax:
                secondMax = childRes
            self.res = max(self.res, firstMax + secondMax)
        return 1 + firstMax
