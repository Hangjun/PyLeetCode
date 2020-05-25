"""
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
Example 1:

Input: 
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"
 

Example 2:

Input: 
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"
 

Constraints:

The given dict won't contain duplicates, and its length won't exceed 100.
All the strings in input have length in range [1, 1000].
Note: This question is the same as 758: https://leetcode.com/problems/bold-words-in-string/
"""

# Time: O(mnk), m = |s|, n = |dict|, k = average length of words. Space: O(n).
class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        bold = [False for _ in range(len(s))]
        # O(mnk) time: m = |s|, n = |dict|, k = average length of words
        for word in dict:
            start = s.find(word)
            while start != -1:
                for i in range(start, start+len(word)):
                    bold[i] = True
                # find the next possible match location
                start = s.find(word, start+1)
        
        res = ""
        i = 0
        while i < len(s):
            if bold[i]:
                res += "<b>"
                while i < len(s) and bold[i]:
                    res += s[i]
                    i += 1
                res += "</b>"
            else:
                res += s[i]
                i += 1
        return res
