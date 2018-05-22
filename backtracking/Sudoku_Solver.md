# 037. Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

- Each of the digits 1-9 must occur exactly once in each row.
- Each of the digits 1-9 must occur exactly once in each column.
- Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
- Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

- The given board contain only digits 1-9 and the character '.'.
- You may assume that the given Sudoku puzzle will have a single unique solution.
- The given board size is always 9x9.

## Method:

backtracking, test valid and recursively call solve:

    class Solution(object):
        def solveSudoku(self, board):
            """
            :type board: List[List[str]]
            :rtype: void Do not return anything, modify board in-place instead.
            """
            
            def isValid(i, j, s):
                for idx in range(9):
                    if board[i][idx]==s:
                        return False
                    if board[idx][j]==s:
                        return False
                    if board[(i/3)*3+idx/3][(j/3)*3+idx%3]==s:
                        return False
                return True
            
            def solve():
                for i in range(len(board)):
                    for j in range(len(board[0])):
                        if board[i][j]=='.':
                            for c in '123456789':
                                if isValid(i, j, c):
                                    board[i][j]=c
                                    if solve():
                                        return True
                                    else:
                                        board[i][j]='.'
                            return False
                return True
            
            solve()