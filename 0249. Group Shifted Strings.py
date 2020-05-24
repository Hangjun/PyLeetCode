"""
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
"""

"""
Analysis: The key to this problem is how to identify strings that are in the same shifting sequence. There are different ways 
to encode this.
In the following code, this manner is adopted: for a string s of length n, we encode its shifting feature as 
"s[1] - s[0], s[2] - s[1], ..., s[n - 1] - s[n - 2],".
Then we build an unordered_map, using the above shifting feature string as key and strings that share the shifting feature as 
value. We store all the strings that share the same shifting feature in a vector. Well, remember to sort the vector since the 
problem requires them to be in lexicographic order :-)
A final note, since the problem statement has given that "az" and "ba" belong to the same shifting sequence. So if 
s[i] - s[i - 1] is negative, we need to add 26 to it to make it positive and give the correct result. 

Time: O(n), Space: O(n).
"""
from collections import defaultdict
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        ht = defaultdict(list)
        for s in strings:
            ht[self.encode(s)].append(s)
        return ht.values()
        
    
    def encode(self, s):
        res = []
        for i in range(1, len(s)):
            diff = ord(s[i]) - ord(s[i-1])
            if diff < 0:
                diff += 26
            res.extend(["a", str(diff)])
        return ":".join(res)
