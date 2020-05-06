"""
Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
"""

# Solution #1: Reservior Sampling. Time: O(n), Space: O(1) - exlucding the data base storage for the array.
from random import randint
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        res = None
        count = 0
        for i, num in enumerate(self.nums):
            if num != target:
                continue
            count += 1
            if randint(0, count-1) == 0:
                res = i
        
        return res
 
 # Solution #2: Hash Table. Time: O(1), Space: O(n). Store the indices that each number appears at. This is good for static queries.
 from collections import defaultdict
from random import randint
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.ht = defaultdict(list)
        for i, num in enumerate(nums):
            self.ht[num].append(i)
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        ind = randint(0, len(self.ht[target])-1)
        return self.ht[target][ind]
 
