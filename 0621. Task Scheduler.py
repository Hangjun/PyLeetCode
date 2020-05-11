"""
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

 

Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
 

Constraints:

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""

"""
Similar to Problem 358	Rearrange String k Distance Apart.
Greedy Algorithm. Time: O(nlogn), Space: O(n).
"""
from collections import Counter, deque
from heapq import heapify, heappush, heappop
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter = Counter(tasks)
        waitQueue = deque([])
        heap = [(-count, taskId) for taskId, count in counter.items()]
        heapify(heap)
        time = 0
        while heap:
            k = n+1
            while k > 0 and heap:
                curCount, curTask = heappop(heap)
                curCount = -curCount
                curCount -= 1
                k -= 1
                time += 1
                if curCount > 0:
                    waitQueue.append((curTask, curCount))
            # put all tasks in waitQueue back to heap
            while waitQueue:
                taskId, count = waitQueue.popleft()
                heappush(heap, (-count, taskId))
            if not heap:
                break
                
            # k equals the remaining idle cycles
            time = time + k

        return time
