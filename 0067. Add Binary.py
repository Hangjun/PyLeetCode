"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.
"""

# Bit-by-bit Compuation using Carry. Time: O(m+n), Space: O(1).
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        carry = 0
        res = []
        for i in range(n-1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
            if carry % 2 == 1:
                res.append('1')
            else:
                res.append('0')
            carry //= 2
        if carry == 1:
            res.append('1')
        res.reverse()
        
        return ''.join(res)
        
# Solution #2: Bit Manipulation. Time: O(m+n), Space: O(max(m, n)).
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x, y = int(a, 2), int(b, 2)
        while y:
            x, y = x ^ y, (x & y) << 1
        return bin(x)[2:]
