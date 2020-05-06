"""
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""

"""
Depending on which of the two matrices are more sparse, we can process A to AReduce that only contains the indices of non-zero 
entries, and process B to BReduce to hash each non-zero elements into each row. The total time to process is O(mn + nk), where 
mxn is the dimension of A and nxk is the dimension of B. The actual time to get the product is total number of non-zero entries 
in A times the average number of non-zero entries per row.

Time: O(mn + nk), Space: O(mn + nk).
"""
from collections import defaultdict
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n, k = len(A), len(A[0]), len(B[0])
        res = [[0 for i in range(k)] for j in range(m)]
        AReduce = []
        for i in range(m):
            for j in range(n):
                if not A[i][j]:
                    continue
                AReduce.append((i, j))
        
        BReduce = defaultdict(list)
        for i in range(n):
            for j in range(k):
                if not B[i][j]:
                    continue
                BReduce[i].append(j)
        
        for x1, y1 in AReduce:
            for y2 in BReduce[y1]:
                res[x1][y2] += A[x1][y1] * B[y1][y2]
        
        return res
