"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

"""
We traverse the input array twice. For the first pass, for each nums[i], we negate nums[nums[i]-1], if it is not negated. This is 
the (nums[i])th number in the array. For instance, if nums[i] = 7, we negate the 7th number in the array, which is nums[6]. Now 
we traverse the array the second time. For each nums[i], being the (i+1)th number, if it is negative, that means the value (i+1) 
must be present in the array. Otherwise (i+1) is missing.

Time: O(n), Space: O(1).
"""
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = []
        for i in range(n):
            j = abs(nums[i])-1
            if nums[j] > 0:
                nums[j] *= -1
        for i in range(1, n+1):
            if nums[i-1] > 0:
                res.append(i)
        return res
