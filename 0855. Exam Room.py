"""
In an exam room, there are N seats in a single row, numbered 0, 1, 2, ..., N-1.

When a student enters the room, they must sit in the seat that maximizes the distance to the closest person.  If there are multiple such seats, they sit in the seat with the lowest number.  (Also, if no one is in the room, then the student sits at seat number 0.)

Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat() returning an int representing what seat the student sat in, and ExamRoom.leave(int p) representing that the student in seat number p now leaves the room.  It is guaranteed that any calls to ExamRoom.leave(p) have a student sitting in seat p.

 

Example 1:

Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
Output: [null,0,9,4,2,null,5]
Explanation:
ExamRoom(10) -> null
seat() -> 0, no one is in the room, then the student sits at seat number 0.
seat() -> 9, the student sits at the last seat number 9.
seat() -> 4, the student sits at the last seat number 4.
seat() -> 2, the student sits at the last seat number 2.
leave(4) -> null
seat() -> 5, the student sits at the last seat number 5.

Note:

1 <= N <= 10^9
ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times across all test cases.
Calls to ExamRoom.leave(p) are guaranteed to have a student currently sitting in seat number p.
"""

# Heap. Time: both seat() and leave() in O(logn) time. Space: O(n).
from heapq import heapify, heappush, heappop

class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.heap = []
        self.available_first = {}
        self.available_last = {}
        self.n = N
        self.push_segment(0, self.n-1)
        
    def push_segment(self, first, last):
        # only one side is occupied
        if first == 0 or last == self.n-1:
            priority = last - first
        else:
            priority = (last - first) / 2
        segment = [-priority, first, last, True]
        heappush(self.heap, segment)
        self.available_first[first] = segment
        self.available_last[last] = segment
            
    def seat(self):
        """
        :rtype: int
        """
        # retrieve the first available segment with highest priority
        while True:
            _, first, last, isValid = heappop(self.heap)
            if isValid:
                del self.available_first[first]
                del self.available_last[last]
                break
        
        if first == 0:
            res = first
            if first != last:
                self.push_segment(first+1, last)
        elif last == self.n-1:
            res = last
            if first != last:
                self.push_segment(first, last-1)
        else:
            res = first + (last-first) / 2
            if first < res:
                self.push_segment(first, res-1)
            if last > res:
                self.push_segment(res+1, last)

        return res
        
    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        # find extending available segments, mark them as invalid, create a merged segment, push it in
        first = last = p
        left, right = p-1, p+1
        if left >= 0 and left in self.available_last:
            left_segment = self.available_last.pop(left)
            left_segment[3] = False
            first = left_segment[1]
        
        if right <= self.n-1 and right in self.available_first:
            right_segment = self.available_first.pop(right)
            right_segment[3] = False
            last = right_segment[2]
        
        self.push_segment(first, last)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
