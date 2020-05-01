"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""

# DFS. Time: O(mn), Space: O(mn). 3 Passes.
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        # Step 1: find all Os reachable from the boundary - those are not captured
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m-1 or j == n-1) and board[i][j] == 'O':
                    self.dfs(board, i, j, board[i][j], 'Y')
        
        # Step 2: find all the internal Os and capture them
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    self.dfs(board, i, j, board[i][j], 'X')
        
        # Step 3: revert all the boundary reachable Y's to Os
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m-1 or j == n-1) and board[i][j] == 'Y':
                    self.dfs(board, i, j, board[i][j], 'O')
    
    # Change boundary reachable Os to Ys - they are not captured
    def dfs(self, board, x, y, old, new):
        board[x][y] = new
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == old:
                self.dfs(board, nx, ny, old, new)
