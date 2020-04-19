"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note:
You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.
Answers within 10^-5 of the actual value will be accepted as correct.
"""

"""
We immedidately think of using the min-max heap trick to solve this problem. Since we are dealing with a sliding window, we need 
an extra data structure to make sure we are only looking at a particular sliding window at a time. Deque is the perfect data 
structure for this booking keeping.

Sliding Window + Priority Queue + Deque. Time: O(nk), Space: O(k).
"""
from heapq import heappush, heappop, heapify
from collections import deque

class MedianFinder:
    def __init__(self, k):
        # min-max priorities queues to compute the median
        self.min_heap = []
        self.max_heap = []
        self.nums = deque([]) # to keep track of the sliding window of size k
        self.k = k
    
    # Time: O(k)
    def add(self, val):
        self.nums.append(val)
        
        # we propogate the incoming number into the (bottom) max heap through the (top) min heap
        heappush(self.min_heap, val)
        # by default Python's heap is min heap, thus need to negate the numbers to turn it into a max heap
        heappush(self.max_heap, -heappop(self.min_heap))
        
        # maintain the sliding window to have size k
        while len(self.nums) > self.k:
            val = self.nums.popleft()
            if val in self.min_heap:
                self.min_heap.remove(val) # O(k)
                heapify(self.min_heap) # O(k)
                heappush(self.min_heap, -heappop(self.max_heap)) # O(logk)
            else:
                self.max_heap.remove(-val) # O(k)
                heapify(self.max_heap) # O(k)
                heappush(self.max_heap, -heappop(self.min_heap)) # O(logk)
        
        # balance the two heaps so that |max_heap| <= |min_heap| <= |max_heap| + 1
        if len(self.max_heap) > len(self.min_heap):
            heappush(self.min_heap, -heappop(self.max_heap))
    
    # Time: O(1)
    def findMedian(self):
        n = len(self.min_heap) + len(self.max_heap)
        if n % 2:
            return self.min_heap[0]
        else:
            return (self.min_heap[0] - self.max_heap[0]) / 2.0

class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        medianFinder = MedianFinder(k)
        res = []
        
        for i in range(len(nums)):
            medianFinder.add(nums[i])
            if i >= k-1:
                res.append(medianFinder.findMedian())
        
        return res
