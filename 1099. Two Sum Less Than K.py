"""
Given an array A of integers and integer K, return the maximum S such that there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation, return -1.

 

Example 1:

Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation: 
We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: A = [10,20,30], K = 15
Output: -1
Explanation: 
In this case it's not possible to get a pair sum less that 15.
 

Note:

1 <= A.length <= 100
1 <= A[i] <= 1000
1 <= K <= 2000
"""

# Sort + Two Pointers. Time: O(nlogn), Space: O(1).
class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        res = -1
        n = len(A)
        if n < 2:
            return res
        diff = sys.maxint
        A.sort()
        left, right = 0, n-1
        while left < right:
            curSum = A[left] + A[right]
            if curSum >= K:
                right -= 1
            else:
                left += 1
                if K - curSum < diff:
                    diff = K - curSum
                    res = curSum
        return res
