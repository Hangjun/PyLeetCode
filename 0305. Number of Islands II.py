"""
A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
Output: [1,1,2,3]
Explanation:

Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
Follow up:

Can you do it in time complexity O(k log mn), where k is the length of the positions?
"""

"""
We use Union-Find to solve this problem. The time complexity is difficult to analyze if we implement the Union-Find with both 
path compression and rank. One caveat is that, if the incoming node has appeared earlier, then we do not need to go through the 
union-find process anymore.
"""
class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        grid = [[0 for i in range(n)] for j in range(m)]
        parent = {}
        rank = {}
        self.count = 0
        
        def find(x):
            if parent[x] != x:
                return find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py: 
                return
            if rank[px] < rank[py]:
                px, py = py, px
            # WLOG assume px has higher or equal rank than py
            parent[py] = px
            rank[px] += rank[px] == rank[py]
            self.count -= 1 # decrement the number of island after the union
        
        res = []
        for i, j in positions:
            print (i, j)
            # (i, j) is already 1, no need to udpate
            if grid[i][j] == 1:
                res.append(self.count)
                continue
            grid[i][j] = 1
            x = parent[x] = i, j
            rank[x] = 0
            self.count += 1
            for y in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                if y in parent:
                    union(x, y)
            res.append(self.count)
        
        return res
