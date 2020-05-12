"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""

# Sort and Heap. Time: O(nlogn), Space: O(n).
from heapq import heapify, heappush, heappop
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        heap = []
        for interval in intervals:
            curStart, curEnd = interval
            if not heap:
                heappush(heap, [curEnd, curStart])
            else:
                lastEnd, lastStart = heappop(heap)
                if curStart >= lastEnd:
                    lastEnd = curEnd # just update the last meeting to end at curEnd
                else:
                    heappush(heap, (curEnd, curStart))
                # push the (possibly) updated last meeting back to the heap
                heappush(heap, (lastEnd, lastStart))
        return len(heap)
