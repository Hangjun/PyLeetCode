"""
Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.

 

Example 1:

Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
Example 2:

Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
 

Note:

1 <= points.length <= 500
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
All points are distinct.
"""

# For each pair of points, determine whether they can form a rectangle being the two vertices on the diagonal. 
# Time: O(n^2), Space: O(n^2).
class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        pointSet = set(map(tuple, points))
        area = float('inf')
        for x1, y1 in points:
            for x2, y2 in points:
                if x1 != x2 and y1 != y2:
                    if (x1, y2) in pointSet and (x2, y1) in pointSet:
                        area = min(area, abs(x1-x2) * abs(y1-y2))
        return area if area < float('inf') else 0
