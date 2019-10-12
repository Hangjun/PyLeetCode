"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4 

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1
Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""

# DFS Solution. We build the adjacency graph first.
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        def dfs(i, adj, visited):
            if not visited[i]:
                visited[i] = True
                for j in adj[i]:
                    dfs(j, adj, visited)
                return 1
            return 0

        adj = [[] for i in range(n)]
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        visited = [False] * n
        return sum(dfs(i, adj, visited) for i in range(n))

# BFS Solution:
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        def bfs(i, visited):
            if visited[i]:
                return 0
            visited[i] = True
            q = [i]
            while q:
                cur = q.pop()
                # level order traverse all neighboring nodes of cur
                for j in adj[cur]:
                    if not visited[j]:
                        visited[j] = True
                        q.append(j)
            return 1
                
        adj = {i: [] for i in range(n)}
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
            
        visited = [False] * n
        return sum(bfs(i, visited) for i in range(n))

# Union-Find Solution:
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
    
        def union(edge):
            px, py = map(find, edge)
            if rank[px] < rank[py]:
                parent[px] = py
            else:
                parent[py] = px
                if rank[px] == rank[py]:
                    rank[px] += 1
        
        parent, rank = range(n), [0] * n
        map(union, edges)
        # return the number of distinct parents
        return len({find(x) for x in parent})
