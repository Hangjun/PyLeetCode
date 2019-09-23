"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

# DFS. Time: O(mn), Space: O(mn)
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        if not board or not board[0]:
            return False
        m, n = len(board), len(board[0])
        visited = [[False] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.dfs(board, word, i, j, 1, visited):
                        return True
                    
        return False
    
    def dfs(self, board, word, x, y, start, visited):
        if start == len(word):
            return True
        visited[x][y] = True
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not self.inBound(board, nx, ny) or visited[nx][ny] or board[nx][ny] != word[start]:
                continue
            if self.dfs(board, word, nx, ny, start+1, visited):
                return True

        visited[x][y] = False
        return False
    
    def inBound(self, board, x, y):
        m, n = len(board), len(board[0])
        return x >= 0 and x < m and y >= 0 and y < n
