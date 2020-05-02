"""
A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Example:

Input: 

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 6 

Explanation: Given three people living at (0,0), (0,4), and (2,2):
             The point (0,2) is an ideal meeting point, as the total travel distance 
             of 2+2+2=6 is minimal. So return 6.
"""

"""
This problem is essentially the same as Problem 317	Shortest Distance from All Buildings. However, if we use BFS to compute all 
the distances like in that problem, it would take O(m^2n^2) time which would result in TLE for this problem. From a computational 
geometric standpoint, the best meeting point (x, y) has coordinate (x_med, y_med), which x_med is the _median_ x-coordinate of 
all the points and y_med is the median y-coordinate of all the points. Hence this problem can be solved by first computing the 
medians and then sum up the Manhattan distances.

To compute the median without having to either sort the coordinates or use fancy linear time selection algorithms, we can run 
two passes through the grid, once row first and once column first to ensure that grid[i][j] == 1 points are collected in the 
coordinate-increasing order, row and column, respectively. Then we can get the median in O(1) time and then sum up the distances.

Another solution with the same running time observes that we can we directly compute the total Manhattan distance without having 
to find the median: we simply compute the diffs between the two points on the two ends consecutively, which is equivalent to 
taking the diffs with the median point.

Time: O(mn), Space: O(max(m, n)).
"""
class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        rowCoords = []
        colCoords = []
        # get the row coordinates in sorted order
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rowCoords.append(i)
        
        # get the col coordinates in sorted order
        for j in range(n):
            for i in range(m):
                if grid[i][j] == 1:
                    colCoords.append(j)
        
        rowMedian = rowCoords[len(rowCoords)/2]
        colMedian = colCoords[len(colCoords)/2]
        
        return self.minTotalDistance1D(rowCoords, rowMedian) + self.minTotalDistance1D(colCoords, colMedian)
    
    def minTotalDistance1D(self, coords, median):
        dist = 0
        for n in coords:
            dist += abs(n - median)
        return dist
        
# Two Pointer solution without having to compute the median:
class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        rowCoords = []
        colCoords = []
        # get the row coordinates in sorted order
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rowCoords.append(i)
        
        # get the col coordinates in sorted order
        for j in range(n):
            for i in range(m):
                if grid[i][j] == 1:
                    colCoords.append(j)
        
        return self.minTotalDistance1D(rowCoords) + self.minTotalDistance1D(colCoords)
    
    def minTotalDistance1D(self, coords):
        dist = 0
        i, j = 0, len(coords)-1
        while i < j:
            dist += coords[j] - coords[i]
            i +=1 
            j -= 1
        return dist
