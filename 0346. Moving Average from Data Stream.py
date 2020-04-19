"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""

# Sliding Window + Deque. Time: O(n), Space: O(n).
from collections import deque
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.nums = deque([])
        self.sum = 0
        self.size = size
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.sum += val
        self.nums.append(val)
        if len(self.nums) > self.size:
            self.sum -= self.nums.popleft()
        
        return self.sum * 1.0 / len(self.nums)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

