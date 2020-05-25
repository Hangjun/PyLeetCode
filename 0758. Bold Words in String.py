"""
Given a set of keywords words and a string S, make all appearances of all keywords in S bold. Any letters between <b> and </b> tags become bold.

The returned string should use the least number of tags possible, and of course the tags should form a valid combination.

For example, given that words = ["ab", "bc"] and S = "aabcd", we should return "a<b>abc</b>d". Note that returning "a<b>a<b>b</b>c</b>d" would use more tags, so it is incorrect.

Constraints:

words has length in range [0, 50].
words[i] has length in range [1, 10].
S has length in range [0, 500].
All characters in words[i] and S are lowercase letters.
Note: This question is the same as 616: https://leetcode.com/problems/add-bold-tag-in-string/
"""

class Solution(object):
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        bold = [False for _ in range(len(S))]
        # O(mnk) time: m = |S|, n = |words|, k = average length of words
        for word in words:
            start = S.find(word)
            while start != -1:
                for i in range(start, start+len(word)):
                    bold[i] = True
                # find the next possible match location
                start = S.find(word, start+1)
        
        res = ""
        i = 0
        while i < len(S):
            if bold[i]:
                res += "<b>"
                while i < len(S) and bold[i]:
                    res += S[i]
                    i += 1
                res += "</b>"
            else:
                res += S[i]
                i += 1
        return res
