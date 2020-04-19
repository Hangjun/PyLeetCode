"""
Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
Follow up:
What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?
"""

"""
Following the local-global pattern in part I of this problem, we can use the left pointer to point to the most recent 0 that's 
being flipped. When we hit a 0, if the left pointer is never set, we continue to increment the local curSum, effectively flipping 
the current 0, and at the same time set left to the index of this 0. If left is set, then we need to update the global res, 
and restart the curSum by removing everything we counted prior (and including) left. Previously we zero out curSum, but now we 
only need to zero out everything before and including left.

Time: (n), Space: O(1). This also works with an infinitely data stream.
"""
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curSum, res = 0, 0
        left = -1 # left points to the most recent 0 that's being flipped
        
        for i in range(len(nums)):
            if nums[i]:
                curSum += 1
            else:
                if left >= 0:
                    # update the res
                    res = max(res, curSum)
                    # reset curSum by counting from left+1
                    curSum = i-left
                else:
                    curSum += 1
                left = i
            res = max(res, curSum)
        return res
