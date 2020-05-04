"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
 

Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5
"""

# DFS and directed graph cycle detection. Time: O(V+E), Spaec: O(V+E). We use visited[] to not visit the same path twice.
from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites or not numCourses:
            return True
        adj = defaultdict(list)
        for e in prerequisites:
            adj[e[1]].append(e[0])
        visited = [False for _ in range(numCourses)]
        inStack = [False for _ in range(numCourses)]
        for course in range(numCourses):
            if visited[course]:
                continue
            if self.dfs(course, visited, inStack, adj):
                return False
        return True
    
    # detect whether there is a directed cycle starting from a unvisited course
    def dfs(self, course, visited, inStack, adj):
        visited[course] = True
        inStack[course] = True
        for n in adj[course]:
            if not visited[n]:
                if self.dfs(n, visited, inStack, adj):
                    return True
            elif inStack[n]: # directed cycle found
                return True
            
        # reset inStack when we are done with the current directed DFS
        inStack[course] = False
        return False
        
# BFS + Topological Sort. Time: O(V+E), we visit every vertex and every edge exactly once. Space: O(V+E).
from collections import deque, defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites or not numCourses:
            return True
        ind = [0 for _ in range(numCourses)]
        adj = defaultdict(list)
        for e in prerequisites:
            ind[e[0]] += 1
            adj[e[1]].append(e[0])
        
        queue = deque([])
        totalDeg = 0
        for course in range(numCourses):
            totalDeg += ind[course]
            if not ind[course]:
                queue.append(course)
        if not queue:
            return False
        while queue:
            course = queue.popleft()
            for n in adj[course]:
                ind[n] -= 1
                totalDeg -= 1
                if not ind[n]:
                    queue.append(n)
        
        return totalDeg == 0
