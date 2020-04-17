"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

# Sliding Window. Time: O(m+n), Space: O(1) since we only have lower case alphabetical characters.
from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        if len(s) < len(p):
            return res
        sCount = Counter()
        pCount = Counter(p)
        ns, np = len(s), len(p)
        
        # loop invariant: [i-np+1, i] is the sliding window
        for i in range(ns):
            # add the character on the right
            sCount[s[i]] += 1
            
            # remove the character on the left
            if i >= np:
                if sCount[s[i-np]] == 1:
                    del sCount[s[i-np]] # otherwise it would have value 0 but still lives in the hash table
                else:
                    sCount[s[i-np]] -= 1
            
            # compare array in the sliding window with p
            if pCount == sCount:
                res.append(i-np+1)
        
        return res
