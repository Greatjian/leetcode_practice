# 130. Surrounded Regions

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,

    X X X X
    X O O X
    X X O X
    X O X X

After running your function, the board should be:

    X X X X
    X X X X
    X X X X
    X O X X
    
## Method:

将边位O改为S，然后bfs/dfs将相邻区域均改为S，最后S区域改为O，其余X：

bfs:

    class Solution(object):
        def solve(self, board):
            """
            :type board: List[List[str]]
            :rtype: void Do not return anything, modify board in-place instead.
            """
            if not board:
                return
            
            m, n=len(board), len(board[0])
            deque=collections.deque([])
            for i in range(m):
                for j in range(n):
                    if ((i==0 or i==m-1) or (j==0 or j==n-1)) and board[i][j]=='O':
                        board[i][j]='S'
                        deque.append((i,j))
                 
            while deque:
                i, j=deque.popleft()
                for (di, dj) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if i+di>=0 and i+di<m and j+dj>=0 and j+dj<n and board[i+di][j+dj]=='O':
                        board[i+di][j+dj]='S'
                        deque.append((i+di, j+dj))
                
            for i in range(m):
                for j in range(n):
                    if board[i][j]!='S':
                        board[i][j]='X'
                    else:
                        board[i][j]='O'                       
                        
dfs:

    class Solution(object):
        def solve(self, board):
            """
            :type board: List[List[str]]
            :rtype: void Do not return anything, modify board in-place instead.
            """
            if not board:
                return
            
            def helper(i, j):
                if i<0 or i>=m or j<0 or j>=n:
                    return
                if board[i][j]=='O':
                    board[i][j]='S'
                    helper(i-1, j)
                    helper(i+1, j)
                    helper(i, j-1)
                    helper(i, j+1)
            
            m, n=len(board), len(board[0])
            for i in range(m):
                for j in range(n):
                    if ((i==0 or i==m-1) or (j==0 or j==n-1)) and board[i][j]=='O':
                        helper(i, j)
                                               
            for i in range(m):
                for j in range(n):
                    board[i][j]='X' if board[i][j]!='S' else 'O'
                        