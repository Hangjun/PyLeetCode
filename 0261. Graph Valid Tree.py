"""
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.
"""

"""
An undirected graph is a valid tree if and only if it is fully connected AND it does not contain any cycles. So we need to check for 
these two things. To check whether the graph is fully connected, we can use DFS to count the connected components. We can add 
the cycle detection logic during the DFS.

DFS. Time: O(V+E), Space: O(V+E). 
"""
from collections import defaultdict
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if not edges:
            return n <= 1
        # build adjanecy list
        adj = defaultdict(list)
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        
        seen = set()
        return not self.dfs(0, -1, seen, adj) and len(seen) == n
    
    # invariant: curNode is marked as visited at this point, DFS on its neighbors and
    # return whether we run into a cycle during the DFS
    def dfs(self, curNode, parentNode, seen, adj):
        if curNode in seen:
            return
        seen.add(curNode)
        for n in adj[curNode]:
            if n not in seen:
                if self.dfs(n, curNode, seen, adj):
                    return True
            elif n != parentNode: # cycle found
                return True
        return False
        
# We actually do not need to explicitly test for cycles. A fully connected graph with exactly n-1 edges cannot have any cycles.
# Therefore, we can instead just count the total number of edges and verify that the graph is fully connected.
# Time: O(V), Space: O(V) - since we know that if E != V-1, we return False immmediately.
from collections import defaultdict
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n-1:
            return False
        # build adjanecy list
        adj = defaultdict(list)
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        seen = set()
        self.dfs(0, seen, adj)
        return len(seen) == n
    
    def dfs(self, curNode, seen, adj):
        if curNode in seen:
            return
        seen.add(curNode)
        for n in adj[curNode]:
            self.dfs(n, seen, adj)

# Solution #3: Union-Find.
# Time: O(V*alpha(V)), where alpha is the inverse Ackerman function. alpha(V) <= 4. Space: O(V).
from collections import defaultdict
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n-1:
            return False
    
        def find(n):
            if parent[n] != n:
                parent[n] = find(parent[n])
            return parent[n]
        
        # return whether we have merged before to detect cycle
        def union(m, n):
            pm = find(m)
            pn = find(n)
            if pm == pn:
                return True
            if rank[pm] < rank[pn]:
                parent[pm] = pn
            else:
                parent[pn] = pm
                rank[pm] += rank[pm] == rank[pn]
            return False
                    
        parent = range(n)
        rank = [0 for i in range(n)]
        for e in edges:
            if union(e[0], e[1]):
                return False
        return True
