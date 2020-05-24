"""
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
"""

# We evaluate recursively all the possible values by breaking it up at all possible operators. We use a hash table to memorize 
# previously seen expressions.

from collections import defaultdict
class Solution(object):
    def __init__(self):
        self.ht = defaultdict(list)
        
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input in self.ht:
            return self.ht[input]
        res = []
        for i, c in enumerate(input):
            if c in "+-*":
                for a in self.diffWaysToCompute(input[:i]):
                    for b in self.diffWaysToCompute(input[i+1:]):
                        if c == '+':
                            res.append(a + b)
                        elif c == '-':
                            res.append(a - b)
                        else:
                            res.append(a * b)
        if not res:
            res.append(int(input))
        
        self.ht[input] = res
        return res
