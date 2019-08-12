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

# Hash table. Time: O(n), Space: O(n).
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
