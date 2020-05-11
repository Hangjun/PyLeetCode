"""
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
] 

Output: "" 

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""

# Topological Sort with BFS Indegree. 
from collections import defaultdict, deque
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if not words:
            return ""
        if len(words) == 1:
            return words[0]
        inDegree = defaultdict(int)
        adjList = defaultdict(set)
        totalDegree = 0
        n = len(words)
        
        # Step 1: construct the inDegree and adjList
        for word in words:
            for c in word:
                inDegree[c] = 0
        for i in range(n-1):
            s, t = words[i], words[i+1]
            L = min(len(s), len(t))
            for j in range(L):
                if s[j] != t[j]:
                    # directed edge: s[j] -> t[j] to represent s[j] proceeds t[j]
                    if t[j] not in adjList[s[j]]:
                        adjList[s[j]].add(t[j])
                        inDegree[t[j]] += 1
                    break
                # newly added constraints: check t is not a prefix of s
                if j == L-1 and len(s) > len(t):
                    return ""
        # Step 2: found the first layer with inDegree = 0
        queue = deque([])
        for char, ind in inDegree.items():
            totalDegree += ind
            if ind == 0:
                queue.append(char)
        # Step 3: BFS layer by layer to "peel off" characters with ind = 0
        res = []
        # invariant: characters in the queue have ind = 0
        while queue:
            cur = queue.popleft()
            res.append(cur)
            for nc in adjList[cur]:
                inDegree[nc] -= 1
                totalDegree -= 1
                if inDegree[nc] == 0:
                    queue.append(nc)
        return ''.join(res) if not totalDegree else ""
