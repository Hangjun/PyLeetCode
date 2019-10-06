"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

# Hash table. In Python, we cannot hash a list. Instead, we must convert the list to a tuple before hashing.
# Time: O(nmlogm), m = average length of each word. n = number of words in the input strs. Space: O(mn).
from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ht = defaultdict(list)
        for s in strs:
            ht[tuple(sorted(s))] += [s]
        return ht.values()

# We can improve the running time by linearly scanning through each word without sorting:
from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ht = defaultdict(list) # ht[hist] = [words with the same histogram]
        for s in strs:
            # ht[tuple(sorted(s))] += [s]
            hist = [0] * 26
            for c in s:
                hist[ord(c) - ord('a')] += 1
            ht[tuple(hist)] += [s]
        return ht.values()
