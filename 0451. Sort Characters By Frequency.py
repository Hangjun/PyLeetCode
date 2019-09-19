"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
"""

# Solution #1: Hash Table. Time: O(nlogn), Space: O(n).
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_dict = {}
        res = ""
        for c in s:
            s_dict[c] = s_dict.get(c, 0) + 1
        s_dict_sorted = sorted(s_dict, key = s_dict.get, reverse = True)
        for c in s_dict_sorted:
            res += c * s_dict[c]
        return res

# Solution #2: Bucket Sort. Time: O(n), Space: O(n)
from collections import defaultdict

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = defaultdict(int)
        bucket = defaultdict(list)
        for c in s:
            freq[c] += 1
        for k, v in freq.iteritems():
            bucket[v].append(k)
        res = ""
        for i in range(len(s), 0, -1):
            if i in bucket:
                for c in bucket[i]:
                    res += i * c
        return res
