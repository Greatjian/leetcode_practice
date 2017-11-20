# 036. Valid Sudoku

Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

[pic]

A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

## Method:

check for memory using dict() or set():

    class Solution(object):
        def isValidSudoku(self, board):
            """
            :type board: List[List[str]]
            :rtype: bool
            """
            seen=set()
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j]!='.':
                        cur=board[i][j]
                        if (i, cur) in seen or (cur, j) in seen or (i/3, j/3, cur) in seen:
                            return False
                        seen.add((i, cur))
                        seen.add((cur, j))
                        seen.add((i/3, j/3, cur))
            return True
            
or adding into a list and checking for duplicates:

    len(list) == len(set(list))