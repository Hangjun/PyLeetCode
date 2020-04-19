"""
Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s. 

 

Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
Example 2:

Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation: 
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
 

Note:

1 <= A.length <= 20000
0 <= K <= A.length
A[i] is 0 or 1 

Hint:
One thing's for sure, we will only flip a zero if it extends an existing window of 1s. Otherwise, there's no point in doing it, 
right? Think Sliding Window!

Since we know this problem can be solved using the sliding window construct, we might as well focus in that direction for 
hints. Basically, in a given window, we can never have > K zeros, right?

We don't have a fixed size window in this case. The window size can grow and shrink depending upon the number of zeros we have 
(we don't actually have to flip the zeros here!).

The way to shrink or expand a window would be based on the number of zeros that can still be flipped and so on.
"""

# Following the hint, this problem is equivalent to finding the longest subarray with at most K zeros. We have done this in 
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/.
# Two Pointer Sliding Window. Time: O(n), Space: O(1).
class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        left = 0
        zeroCount = 0
        res = 0
        for right in range(len(A)):
            if A[right] == 0:
                zeroCount += 1
            # shrink left to find the longest subarray with at most K zeros
            while zeroCount > K:
                if A[left] == 0:
                    zeroCount -= 1
                left += 1
            res = max(res, right-left+1)
        return res
