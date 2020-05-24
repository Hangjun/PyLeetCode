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
        carry = 0
        res = []
        i = len(num1)-1
        j = len(num2)-1
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(num1[i])
            if j >= 0:
                carry += int(num2[j])
            res.append(str(carry%10))
            carry /= 10
            i -= 1
            j -= 1
        if carry:
            res.append('1')
        return ''.join(res[::-1])

