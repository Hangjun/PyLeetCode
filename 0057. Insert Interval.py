"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""

# After we find the location to insert the newInterval, we still need to consider subsequent intervals. This suggests we do this 
# iteratively. Time: O(n), Space: O(1).
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []
        i = 0
        while i < len(intervals):
            curInterval = intervals[i]
            if newInterval[1] < curInterval[0]:
                break
            if curInterval[1] < newInterval[0]:
                res.append(curInterval)
            else:
                newInterval[0] = min(newInterval[0], curInterval[0])
                newInterval[1] = max(newInterval[1], curInterval[1])
            i += 1
        
        res.append(newInterval)
        # append the rest of the intervals
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        return res
