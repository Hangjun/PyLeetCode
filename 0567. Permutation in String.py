"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""

# Sliding Window. Time: O(m+n), Space: O(1).
from collections import defaultdict
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if (len(s1) > len(s2)):
            return False
        hist = defaultdict(int)
        for i in range(len(s1)):
            hist[s1[i]] += 1
            hist[s2[i]] -= 1
        if self._allZero(hist):
            return True
        
        # loop invariant: [j-len(s1), j-1] has been checked
        for j in range(len(s1), len(s2)):
            hist[s2[j-len(s1)]] += 1
            hist[s2[j]] -= 1
            if self._allZero(hist):
                return True
        
        return False
        
    def _allZero(self, hist):
        for _, value in hist.items():
            if value:
                return False
        return True

# We can obsorb the "warm up" into a single for loop:
from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        count = Counter(s1)
    
        # loop invariant: sliding window is [i-n1+1, i]
        for i in range(n2):
            if i < n1:
                count[s2[i]] -= 1
            else:
                count[s2[i]] -= 1
                count[s2[i-n1]] += 1
            if self._allZero(count):
                return True

        return False

    def _allZero(self, count):
        for _, value in count.items():
            if value:
                return False
        return True

"""
This problem is actually the same as https://github.com/Hangjun/PyLeetCode/blob/master/0438.%20Find%20All%20Anagrams%20in%20a%20String.py. 
We can also use two hash tables and have the same implementation:
Time: O(m+n), Space: O(1)
"""
from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        count1 = Counter(s1)
        count2 = Counter()
        
        # loop invariant: sliding window [i-n1+1, i]
        for i in range(n2):
            count2[s2[i]] += 1
            if i >= n1:
                if count2[s2[i-n1]] == 1:
                    del count2[s2[i-n1]]
                else:
                    count2[s2[i-n1]] -= 1
            if count2 == count1:
                return True
        
        return False
