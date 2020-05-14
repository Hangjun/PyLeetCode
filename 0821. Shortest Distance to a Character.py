"""
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
"""

# BFS. Time: O(n), Space: O(n). Be careful about the loop invariant so we do not double-increment the distance from two curNodes.
from collections import deque
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        res = [-1 for _ in range(len(S))]
        queue = deque([])
        for i, c in enumerate(S):
            if c == C:
                queue.append(i)
                res[i] = 0
        distance = 1
        # BFS to fill the res
        # invariant: the current level's distance has been calculated
        while queue:
            curSize = len(queue)
            for _ in range(curSize):
                curInd = queue.popleft()
                for ni in [curInd-1, curInd+1]:
                    if 0 <= ni < len(S) and res[ni] == -1:
                        res[ni] = distance
                        queue.append(ni)
            distance += 1
        return res
