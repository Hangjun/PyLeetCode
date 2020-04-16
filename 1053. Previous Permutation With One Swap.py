"""
Given an array A of positive integers (not necessarily distinct), return the lexicographically largest permutation that is smaller than A, that can be made with one swap (A swap exchanges the positions of two numbers A[i] and A[j]).  If it cannot be done, then return the same array.

Example 1:

Input: [3,2,1]
Output: [3,1,2]
Explanation: Swapping 2 and 1.
Example 2:

Input: [1,1,5]
Output: [1,1,5]
Explanation: This is already the smallest permutation.
Example 3:

Input: [1,9,4,6,7]
Output: [1,7,4,6,9]
Explanation: Swapping 9 and 7.
Example 4:

Input: [3,1,1,3]
Output: [1,3,1,3]
Explanation: Swapping 1 and 3.
 

Note:

1 <= A.length <= 10000
1 <= A[i] <= 10000
"""

"""
The idea is similar to https://github.com/Hangjun/PyLeetCode/blob/master/0031.%20Next%20Permutation.py. We traverse the array 
backwards and find the first A[i-1] > A[i]. A[k] := A[i-1] is the number we want to swap out in order to find the previous 
permutation. We scan A[i:] to find the largest number that is strictly smaller than A[k]. One caveat is that, if there are ties
 (since the numbers are not necessary distinct), we need to swap with the LEFTMOST one, to get the largest possible previous 
 permutation.
 
 Time: O(n), Space: O(1). We can further improve the running time by using a binary search to find the second index. But that 
 won't change the asymptotic running time so we omit the solution here.
"""
class Solution(object):
    def prevPermOpt1(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if not A:
            return A
        
        i = len(A)-1
        while i > 0 and A[i-1] <= A[i]:
            i -= 1
        if i == 0:
            return A
        
        k = i-1
        j = len(A)-1
        while j > k and A[j] >= A[k]:
            j -= 1
        # need the leftmost among ties
        while j > k and A[j-1] == A[j]:
            j -= 1
        A[k], A[j] = A[j], A[k]
        return A

