"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

# Solution #1: Backtracking DFS.
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone_dial = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '}
        res = []
        if not digits:
            return res
        self.combinationDFS(digits, 0, phone_dial, "", res)
        return res
    
    def combinationDFS(self, digits, start, phone_dial, cur, res):
            if start == len(digits):
                res.append(cur)
                return
            for c in phone_dial[digits[start]]:
                self.combinationDFS(digits, start+1, phone_dial, cur + c, res)

# Solution #2: Iterative Construction.
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        phone_dial = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '}
        res = [""]
        for digit in digits:
            tmp = []
            for c in phone_dial[digit]:
                for s in res:
                    s += c
                    tmp.append(s)
            res = tmp
        return res
# The idea is, we iteratively construct the final solution set by appending one character to the existing set's partial strings.
# We can modify our code to be more consise in Python:
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone_dial = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '}
        res = []
        for digit in digits:
            res = [pre + c
                   for pre in res or [""]
                   for c in phone_dial[digit]]
        return res
