"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

# Bucket Sort. Time: O(n), Space: O(n).
from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = defaultdict(int)
        bucket = defaultdict(list)
        for n in nums:
            freq[n] += 1
        # bucket[count] stores numbers that appeared count times
        for num, count in freq.items():
            bucket[count].append(num)
        
        # bucket sort by traversing the count downward
        res = []
        for count in range(len(nums), 0, -1):
            if count in bucket:
                for num in bucket[count]:
                    if len(res) == k:
                        return res
                    res.append(num)
        return res
    
# Heap Sort. Time: O(n + klogn), Space: O(n)
from collections import Counter
from heapq import heapify, heappush, heappop
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)
        heap = [(-freq, num) for (num, freq) in count.items()]
        heapify(heap)
        return [heappop(heap)[1] for _ in range(k)]
    
# Heap Sort. Time: O(n + klogk), Space: O(k).
from collections import Counter
from heapq import heapify, heappush, heappop
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)
        heap = []
        for num, freq in count.items():
            if len(heap) < k:
                heappush(heap, (freq, num))
            else:
                heappushpop(heap, (freq, num))
        
        return [heappop(heap)[1] for _ in range(k)]

# Another solution is to use Python's built-in Counter data structure
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return zip(*collections.Counter(nums).most_common(k))[0]
