"""
Given an array A of non-negative integers, return the maximum sum of elements in two non-overlapping (contiguous) subarrays, which have lengths L and M.  (For clarification, the L-length subarray could occur before or after the M-length subarray.)

Formally, return the largest V for which V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1] + ... + A[j+M-1]) and either:

0 <= i < i + L - 1 < j < j + M - 1 < A.length, or
0 <= j < j + M - 1 < i < i + L - 1 < A.length.
 

Example 1:

Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
Output: 20
Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.
Example 2:

Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
Output: 29
Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.
Example 3:

Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
Output: 31
Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with length 3.
 

Note:

L >= 1
M >= 1
L + M <= A.length <= 1000
0 <= A[i] <= 1000
"""

# Time: O(n), Space: O(n). Use a prefix sum array.
class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        n = len(A)
        prefixSum = A
        for i in range(1, n):
            prefixSum[i] += prefixSum[i-1]
        
        LMax = prefixSum[L-1] # max sum of consecutive subarray of size L before the last M elements
        MMax = prefixSum[M-1] # max sum of consecutive subarray of size M before the last L elements
        res = prefixSum[L+M-1]
            
        for i in range(L+M, n):
            # update LMax with the current M element window of A[i-m+1]...A[i]
            # the window L is A[i-m-l+1], ..., A[i-m]
            LMax = max(LMax, prefixSum[i-M] - prefixSum[i-M-L])
            
            # update MMax with the current L element window of A[i-l+1]...A[i]
            # the window M is A[i-m-l+1],..., A[i-l]
            MMax = max(MMax, prefixSum[i-L] - prefixSum[i-M-L])
            
            # update res with the current L + M window combinations
            res = max(res, LMax + prefixSum[i] - prefixSum[i-M], MMax + prefixSum[i] - prefixSum[i-L])
        
        return res

