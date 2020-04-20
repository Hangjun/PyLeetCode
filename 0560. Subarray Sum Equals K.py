"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

"""
Inspired by https://github.com/Hangjun/PyLeetCode/blob/master/0523.%20Continuous%20Subarray%20Sum.py, this time we need to use 
the hash table differently. It turns out that if we let the key, value be curSum -> #times this curSum appeared as we linearly 
scan the array while computing the accumulative sum. Then if curSum-k exists in this hash table, then it means that there must 
have been at least one subarray previously whose sum is curSum-k, indicating that the partial sum from that subarray onward to 
the current index is exactly k!!

Hash table. Partial Sum Subarray. Time: O(n), Space: O(n).
"""
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sumCount = {0: 1}
        count = 0
        curSum = 0
        for n in nums:
            curSum += n
            if curSum - k in sumCount:
                count += sumCount[curSum-k]
            sumCount[curSum] = sumCount.get(curSum, 0) + 1
        return count
