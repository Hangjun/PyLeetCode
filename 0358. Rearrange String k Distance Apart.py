"""
Given a non-empty string s and an integer k, rearrange the string such that the same characters are at least distance k from each other.

All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".

Example 1:

Input: s = "aabbcc", k = 3
Output: "abcabc" 
Explanation: The same letters are at least distance 3 from each other.
Example 2:

Input: s = "aaabc", k = 3
Output: "" 
Explanation: It is not possible to rearrange the string.
Example 3:

Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least distance 2 from each other.
"""

"""
Similar to Problem 767 Reorganize String (k = 2 case), we need some book-keeping to know when we can re-use a character with 
positive count again. In Problem 767, we hanled it very manually in the if-else construct. More generally, we can use a scheduling 
queue to store temporarily unavailable tasks. This is a very useful algorithmic construct. Memorize it.

Greedy Algorithm. Time: O(nlogn), Space: O(n).
"""
from collections import Counter, deque
from heapq import heapify, heappush, heappop
class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if not s:
            return ""
        counter = Counter(s)
        heap = [(-count, char) for char, count in counter.items()]
        heapify(heap)
        waitQueue = deque([])
        res = []
        while heap:
            curCount, curChar = heappop(heap)
            curCount = -curCount
            res.append(curChar)
            curCount -= 1
            # place curChar into the waitQueue
            waitQueue.append((curChar, curCount))
            if len(waitQueue) < k:
                continue
            # front of the waitQueue is ready to be pushed back into the heap
            readyChar, readyCount = waitQueue.popleft()
            if readyCount > 0:
                heappush(heap, (-readyCount, readyChar))
        return ''.join(res) if len(res) == len(s) else ""
