"""
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]
"""

# Greedy Algorithm. Time: O(n) Two-Pass, Space: O(n).
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_array = map(int, str(num))
        # last_occured_index[n] = index of the last occurrence of n
        last_occured_index = {n : i for i, n in enumerate(num_array)}
        
        # greedily swap the biggest number larger than the current from the last possible location
        for i, n in enumerate(num_array):
            for d in range(9, n, -1):
                if d not in last_occured_index:
                    continue
                if last_occured_index[d] > i:
                    num_array[i], num_array[last_occured_index[d]] = num_array[last_occured_index[d]], num_array[i]
                    return int(''.join(map(str, num_array)))
        return num
        
