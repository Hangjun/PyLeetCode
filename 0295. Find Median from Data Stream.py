"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 

Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
"""

"""
This is a simplier version of https://github.com/Hangjun/PyLeetCode/blob/master/0480.%20Sliding%20Window%20Median.py. We maintain 
a min-max heap structure and a |max_heap| <= |min_heap| <= |max_heap| + 1 property.
"""
from heapq import heapify, heappush, heappop
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []
        
    
    # Time: O(n)
    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heappush(self.min_heap, num)
        heappush(self.max_heap, -heappop(self.min_heap))
        
        # maintain |max_heap| <= |min_heap| <= |max_heap| + 1
        if len(self.max_heap) > len(self.min_heap):
            heappush(self.min_heap, -heappop(self.max_heap))
        

    # Time: O(1)
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2.0
        else:
            return self.min_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
