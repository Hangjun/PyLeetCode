"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

# Bit-by-bit Addition. Time: O(m+n), Space: O(max(m, n)).
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = []
        num1, num2 = num1[::-1], num2[::-1]
        n = max(len(num1), len(num2))
        carry = 0
        for i in range(n):
            # compute current digit sum
            if i < len(num1):
                carry += int(num1[i])
            if i < len(num2):
                carry += int(num2[i])
            res.append(str(carry % 10))
            carry //= 10
        
        if carry:
            res.append('1')
        
        # concatnate and reverse
        return ''.join(res)[::-1]
