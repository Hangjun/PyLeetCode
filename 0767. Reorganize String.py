"""
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
"""

"""
This is a typical Greedy algorithm problem. We first sort the character frequencies and try to fill the string from the most 
frequent characters. If we ever run into the same character, we try to fetch the second frequent character. This suggests that 
we use a hash table to store the character frequencies and use a heap to handle the ordering.

Time: O(nlogn), Space: O(n).
"""
from collections import Counter
from heapq import heapify, heappush, heappop
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return ""
        counter = Counter(S)
        heap = [(-count, c) for c, count in counter.items()]
        heapify(heap)
        res = []
        while heap:
            firstCount, firstChar = heappop(heap)
            if not res or res[-1] != firstChar:
                res.append(firstChar)
                firstCount += 1
                if firstCount < 0:
                    heappush(heap, (firstCount, firstChar))
            else: # adjacent character is the same, push the heap again
                if not heap:
                    return ""
                secondCount, secondChar = heappop(heap)
                res.append(secondChar)
                secondCount += 1
                if secondCount < 0:
                    heappush(heap, (secondCount, secondChar))
                # CAUTION: need to push firstChar back to heap!
                heappush(heap, (firstCount, firstChar))
        return ''.join(res)
