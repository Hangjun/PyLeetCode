"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
"""

"""
For this type of sliding window problem, we need to calculate certain statistics for each sliding window. Usually heaps (median) 
or deque (min/max) are used. There are three steps involved:
1. Add the new data into the data structure.
2. Adjust the data structure (e.g. maintain balance, ordering, or other intrinsic property)
3. Calculate the statistics.

Sliding Window + Deque. Time: O(n), Space: O(k).
"""
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        if not nums or k == 0:
            return res
        # we maintain a decreasing deque storing the indices of the numbers
        dq = deque()
        
        # warm up the deque with the first k numbers
        for i in range(k):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
        
        for i in range(k, len(nums)):
            # add the sliding window max from the _previous_ iteration
            res.append(nums[dq[0]])
            
            # push i into deque
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            
            # reorganize dq as it may contain indices from k-window away
            while dq and dq[0] <= i-k:
                dq.popleft()
        
        # add the last sliding window max
        res.append(nums[dq[0]])
        return res
