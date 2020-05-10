"""
S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.

Example :
Input: 
S = "cba"
T = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.
 

Note:

S has length at most 26, and no character is repeated in S.
T has length at most 200.
S and T consist of lowercase letters only.
"""

# Solution #1: Bruteforce with Sort. Time: O(nlogn), Space: O(n).
from collections import defaultdict
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        n = len(S)
        
        # character -> index
        charToIndex = defaultdict(int)
        for i, c in enumerate(S):
            charToIndex[c] = i
        tmp = []
        residual = []
        for i, c in enumerate(T):
            if c in charToIndex:
                tmp.append(charToIndex[c])
            else: residual.append(c)
        
        tmp.sort()
        
        # use S as a look up table to recover the index -> characer mapping
        for i in range(len(tmp)):
            tmp[i] = S[tmp[i]]
        return ''.join(tmp) + ''.join(residual)

# Solution #2: String S actually already provides up the natural ordering. All we need to do is to take a histogram of T and 
# traverse S to see whether there is a character in S that also exists in T (and get the count from the histogram).
# Time: O(max(m + n)), Space: O(n). m = len(S), n = len(T).
from collections import Counter
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        counter = Counter(T)
        res = []
        residual = []
        for c in S:
            res.append(c * counter[c])
            counter[c] = 0 # import to zero out the count once we have written it to res

        for c, count in counter.items():
            res.append(c * counter[c])
            counter[c] = 0
        return ''.join(res)
