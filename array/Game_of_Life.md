# 289. Game of Life

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

- Any live cell with fewer than two live neighbors dies, as if caused by under-population.
- Any live cell with two or three live neighbors lives on to the next generation.
- Any live cell with more than three live neighbors dies, as if by over-population..
- Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state.

Follow up: 

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.

In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

## Method:

0，1外通过增加2，3表示后轮状态，移位可实现原状态到新状态的转变：

    class Solution(object):
        def gameOfLife(self, board):
            """
            :type board: List[List[int]]
            :rtype: void Do not return anything, modify board in-place instead.
            """
            for i in range(len(board)):
                for j in range(len(board[0])):
                    life=self.countLife(board,i,j)
                    if board[i][j]==1 and (life==2 or life==3):
                        board[i][j]=3
                    if board[i][j]==0 and life==3:
                        board[i][j]=2
            for i in range(len(board)):
                for j in range(len(board[0])):
                    board[i][j]>>=1
    
            
        def countLife(self,board,i,j):
            life=0
            a=[-1,0,1,-1,1,-1,0,1]
            b=[-1,-1,-1,0,0,1,1,1]
            for (di,dj) in zip(a,b):
                if i+di>=0 and i+di<len(board) and j+dj>=0 and j+dj<len(board[0]):
                    life+=board[i+di][j+dj]%2
            return life