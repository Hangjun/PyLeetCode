"""
In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N), with one additional directed edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] that represents a directed edge connecting nodes u and v, where u is a parent of child v.

Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given directed graph will be like this:
  1
 / \
v   v
2-->3
Example 2:
Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
Output: [4,1]
Explanation: The given directed graph will be like this:
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3
Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.
"""

# Union-Find. Time: O(ELogV), Space: O(E+V).
class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        parent = {}
        rank = [0 for _ in range(len(edges)+1)]
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
        
        def detect_cycle(edge):
            u, v = edge
            while u != v and u in parent:
                u = parent[u]
            return u == v
        
        candidates = []
        for u, v in edges:
            if v not in parent:
                parent[v] = u
            else:
                candidates.append([parent[v], v])
                candidates.append([u, v])
        
        if candidates:
            if detect_cycle(candidates[0]):
                return candidates[0]
            else:
                return candidates[1]
        else:
            parent = list(range(len(edges)+1))
            for u, v in edges:
                if not union(u, v):
                    return [u, v]
