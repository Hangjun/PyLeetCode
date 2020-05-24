"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
"""

# DFS + Backtracking. It is easy to miss that fact that we might not be able to recover a complete itinerary from any airport. 
# Therefore we need to implement the backtracking mechnism.

from collections import defaultdict
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        flight_map = defaultdict(list)
        for origin, destination in tickets:
            flight_map[origin].append(destination)
        visited = {}
        for origin, destinations in flight_map.items():
            destinations.sort()
            visited[origin] = [False for _ in range(len(destinations))]
        
        self.res = []
        n = len(tickets)+1
        self.dfs('JFK', flight_map, visited, n, ['JFK'])
        return self.res
    
    def dfs(self, start, flight_map, visited, n, path):
        if len(path) == n:
            self.res = path
            return True
        for i, destination in enumerate(flight_map[start]):
            if not visited[start][i]:
                visited[start][i] = True
                if self.dfs(destination, flight_map, visited, n, path + [destination]):
                    return True
                visited[start][i] = False

        return False
