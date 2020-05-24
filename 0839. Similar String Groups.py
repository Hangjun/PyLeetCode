"""
Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list A of strings.  Every string in A is an anagram of every other string in A.  How many groups are there?

 

Example 1:

Input: A = ["tars","rats","arts","star"]
Output: 2
 

Constraints:

1 <= A.length <= 2000
1 <= A[i].length <= 1000
A.length * A[i].length <= 20000
All words in A consist of lowercase letters only.
All words in A have the same length and are anagrams of each other.
The judging time limit has been increased for this question.
"""

# Union-Find.
from collections import defaultdict, deque

class Solution(object):
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        adjList = defaultdict(list)
        parent = {}
        rank = {}
        
        def find(s):
            if parent[s] != s:
                parent[s] = find(parent[s])
            return parent[s]
        
        def union(s, t):
            ps = find(s)
            pt = find(t)
            if rank[ps] < rank[pt]:
                parent[ps] = pt
            else:
                parent[pt] = ps
                rank[ps] += rank[ps] == rank[pt]

        for s in A:
            parent[s] = s
            rank[s] = 0
            
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                s = A[i]
                t = A[j]
                if self.similar(s, t):
                    union(s, t)
                    
        return len(set(find(s) for s in A))
        
    def similar(self, s, t):
        return sum(a != b for a, b in zip(s, t)) <= 2

# BFS
from collections import defaultdict, deque

class Solution(object):
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        adjList = defaultdict(list)
        for i in range(len(A)):
            for j in range(1, len(A)):
                s = A[i]
                t = A[j]
                if self.similar(s, t):
                    adjList[s].append(t)
                    adjList[t].append(s)
        
        components = 0
        visited = set()
        for s in A:
            if s in visited:
                continue
            visited.add(s)
            queue = deque([s])
            while queue:
                curNode = queue.popleft()
                for nn in adjList[curNode]:
                    if nn not in visited:
                        visited.add(nn)
                        queue.append(nn)
            components += 1
        return components

    def similar(self, s, t):
        return sum(a != b for a, b in zip(s, t)) <= 2
