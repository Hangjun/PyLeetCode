"""
Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

 

Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 

Note:

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000
"""

"""
Exactly same idea as https://github.com/Hangjun/PyLeetCode/blob/master/0560.%20Subarray%20Sum%20Equals%20K.py. We store the mod 
count so that at a given point when a curSum % k exists in the hash table, that means there was a subarray whose sum has the 
same mod k, indicicating that the subarray in the middle is divisible by k.

One important thing to note is that we must initialize the mod_count hash table with {0: 1} so that we do not miss the first 
subarray whose sum is already divisible by k.

Time: O(n), Space: O(n).
"""
class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        mod_count = {0: 1} # this initialization is important!
        count = 0
        curSum = 0
        for n in A:
            curSum += n
            if curSum % K in mod_count:
                count += mod_count[curSum % K]
            mod_count[curSum % K] = mod_count.get(curSum % K, 0) + 1
        return count
