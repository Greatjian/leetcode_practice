# 794. Valid Tic-Tac-Toe State

A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.

Here are the rules of Tic-Tac-Toe:

- Players take turns placing characters into empty squares (" ").
- The first player always places "X" characters, while the second player always places "O" characters.
- "X" and "O" characters are always placed into empty squares, never filled ones.
- The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
- The game also ends if all squares are non-empty.
- No more moves can be played if the game is over.

Example 1:

    Input: board = ["O  ", "   ", "   "]
    Output: false
    Explanation: The first player always plays "X".

Example 2:

    Input: board = ["XOX", " X ", "   "]
    Output: false
    Explanation: Players take turns making moves.

Example 3:

    Input: board = ["XXX", "   ", "OOO"]
    Output: false

Example 4:

    Input: board = ["XOX", "O O", "XOX"]
    Output: true

Note:

- board is a length-3 array of strings, where each string board[i] has length 3.
- Each board[i][j] is a character in the set {" ", "X", "O"}.

## Method:

    class Solution(object):
        def validTicTacToe(self, board):
            """
            :type board: List[str]
            :rtype: bool
            """
            if self.check1(board)!=0 and self.check1(board)!=1:
                return False
            if self.check2(board)!=0 and self.check2(board)!=1 and self.check2(board)!=10:
                return False
            if self.check1(board)==0 and self.check2(board)==10:
                return False
            if self.check1(board)==1 and self.check2(board)==1:
                return False
            return True
            
        def check1(self, board):
            oCount, xCount=0, 0
            for i in board:
                for j in i:
                    if j=='X':
                        xCount+=1
                    if j=='O':
                        oCount+=1
            return xCount-oCount
        
        def check2(self, board):
            xWin, oWin=0, 0
            for i in range(3):
                if board[i][0]==board[i][1]==board[i][2]=='X':
                    xWin+=1
                if board[i][0]==board[i][1]==board[i][2]=='O':
                    oWin+=1
                if board[0][i]==board[1][i]==board[2][i]=='X':
                    xWin+=1
                if board[0][i]==board[1][i]==board[2][i]=='O':
                    oWin+=1
            if board[0][0]==board[1][1]==board[2][2]=='X':
                xWin+=1
            if board[0][0]==board[1][1]==board[2][2]=='O':
                oWin+=1
            if board[0][2]==board[1][1]==board[2][0]=='X':
                xWin+=1
            if board[0][2]==board[1][1]==board[2][0]=='O':
                oWin+=1
            return xWin*10+oWin
            
## Solution:

shorter function: more input
    
    class Solution(object):
        def validTicTacToe(self, board):
            """
            :type board: List[str]
            :rtype: bool
            """
            oCount=sum(row.count('O') for row in board)
            xCount=sum(row.count('X') for row in board)
            if xCount-oCount!=0 and xCount-oCount!=1:
                return False
            if self.win(board, 'O') and self.win(board, 'X'):
                return False
            if self.win(board, 'O') and xCount-oCount==1:
                return False
            if self.win(board, 'X') and xCount-oCount==0:
                return False
            return True
        
        def win(self, board, player):
            for i in range(3):
                if board[i][0]==board[i][1]==board[i][2]==player:
                    return True
                if board[0][i]==board[1][i]==board[2][i]==player:
                    return True
            if board[0][0]==board[1][1]==board[2][2]==player:
                return True
            if board[0][2]==board[1][1]==board[2][0]==player:
                return True
            return False