"""
Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.

 

Example 1:

Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5

Example 2:

Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5

Example 3:

Input: [1,2,3,4,4,5]
Output: False
 

Constraints:

1 <= nums.length <= 10000
"""

# Greedy Algorithm. Time: O(n), Space: O(n).
from collections import Counter
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        left = Counter(nums) # left[n] = number of unused n
        right = Counter() # right[n] = number of consecutive subsequences ending at n
        for n in nums:
            if not left[n]:
                continue
            left[n] -= 1
            if right[n-1] > 0:
                right[n-1] -= 1
                right[n] += 1
            elif left[n+1] > 0 and left[n+2] > 0:
                right[n+2] += 1
                left[n+1] -= 1
                left[n+2] -= 1
            else:
                return False
        return True
