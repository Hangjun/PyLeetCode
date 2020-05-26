"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3
Example 2:
Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
Output: [1,4]
Explanation: The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3
Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.

Update (2017-09-26):
We have overhauled the problem description + test cases and specified clearly the graph is an undirected graph. For the directed graph follow up please see Redundant Connection II). We apologize for any inconvenience caused.
"""

"""
Solution #1: DFS. We construct the adjacency list of this graph. Before adding a new edge to the adjList, we check whether these 
two vertices are already connected via DFS.

In the worst case, for each edge we need to traverse all past edges so the running time is O(n^2).

Time: O(n^2), Space: O(n).
"""
from collections import defaultdict
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        adjList = defaultdict(list)
        for u, v in edges:
            visited = set()
            if u in adjList and v in adjList and self.dfs(u, v, visited, adjList):
                return [u, v]
            adjList[u].append(v)
            adjList[v].append(u)
    
    # dfs to check whether there is a path from source to target
    def dfs(self, source, target, visited, adjList):
        if source == target:
            return True
        visited.add(source)
        for nn in adjList[source]:
            if nn not in visited:
                if self.dfs(nn, target, visited, adjList):
                    return True
        return False
        
"""
Solution #2: Union-Find. Similar to Problem 261	Graph Valid Tree. For each edge, we perform a union of the two nodes and remembber
that we have unioned them. The second time we encounter these two nodes, we know that they are already connected, hence must be 
a duplicating edge.

Time: O(n * alpha(n)) which is approximately O(n). Space: O(n).
"""
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent = {}
        rank = {}
        
        def find(u):
            if parent[u] != u:
                parent[u] =  find(parent[u])
            return parent[u]
        
        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return False
            if rank[pu] < rank[pv]:
                parent[pu] = pv
            else:
                parent[pv] = pu
                rank[pu] += rank[pu] == rank[pv]
            return True
        
        for u, v in edges:
            parent[u] = u
            parent[v] = v
            rank[u] = 0
            rank[v] = 0
            
        for u, v in edges:
            if not union(u, v):
                return [u, v]
