"""
Given a string S, find out the length of the longest repeating substring(s). Return 0 if no repeating substring exists.

 

Example 1:

Input: "abcd"
Output: 0
Explanation: There is no repeating substring.
Example 2:

Input: "abbaba"
Output: 2
Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.
Example 3:

Input: "aabcaabdaab"
Output: 3
Explanation: The longest repeating substring is "aab", which occurs 3 times.
Example 4:

Input: "aaaaa"
Output: 4
Explanation: The longest repeating substring is "aaaa", which occurs twice.
 

Note:

The string S consists of only lowercase English letters from 'a' - 'z'.
1 <= S.length <= 1500
"""

# Bruteforce Solution using Hash Table. Time: O(n^2), Space: O(n^2).
from collections import defaultdict
class Solution(object):
    def longestRepeatingSubstring(self, S):
        """
        :type S: str
        :rtype: int
        """
        # generate all substrings and place them in a hash map
        hashmap = defaultdict(int)
        n = len(S)
        res = 0
        for k in range(1, n):
            # i + k <= n-1 i.e. i <= n-k-1
            for i in range(n-k):
                hashmap[S[i:i+k+1]] += 1
        for s, count in hashmap.items():
            if count < 2:
                continue
            res = max(res, len(s))
        return res

"""
Note that if there exists a duplicate substring of size k, then there also exists a duplicate substring of size k-1. Therefore 
we can optimize the above bruteforce solution using Binary Search to cut the average running time down to O(nlogn).

Time: O(nlogn), Space: O(n^2).
"""
from collections import defaultdict
class Solution(object):
    def longestRepeatingSubstring(self, S):
        """
        :type S: str
        :rtype: int
        """
        left, right = 1, len(S)
        while left <= right:
            mid = left + (right - left) / 2
            if self.search(mid, S) != -1:
                left = mid + 1
            else:
                right = mid - 1
        return left-1
        
    # return whether there is a duplicate substring of size k in S
    def search(self, k, S):
        n = len(S)
        hasSeen = set()
        # S[i ... i+k-1] => i+k-1 <= n-1 => i <= n-k
        for i in range(n-k+1):
            substr = S[i:i+k]
            if substr in hasSeen:
                return i
            hasSeen.add(substr)
        return -1
