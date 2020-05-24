"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""

# DFS with Memorization. Time: O(n^3), Space: O(n^3).
from collections import defaultdict
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # string -> all breakable lists of this string
        self.ht = defaultdict(list)
        return self.dfs(s, set(wordDict))
    
    def dfs(self, s, wordDict):
        # first look in the cache
        if s in self.ht:
            return self.ht[s]
        res = []
        # cut s into s[:l] and s[l:], l = length of the first part of the substring
        # l starts from 1 since wordDict contains non-empty words only
        for l in range(1, len(s)+1):
            prefix = s[:l]
            if prefix not in wordDict:
                continue
            if l == len(s):
                res.append(s)
                break
            suffix = s[l:]
            suffixBreak = self.dfs(suffix, wordDict)
            res.extend([prefix + " " + sb for sb in suffixBreak])
        
        self.ht[s] = res
        return res
