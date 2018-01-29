# 773. Sliding Puzzle

On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

Example 1:

    Input: board = [[1,2,3],[4,0,5]]
    Output: 1
    Explanation: Swap the 0 and the 5 in one move.
    
Example 2:    
    
    Input: board = [[1,2,3],[5,4,0]]
    Output: -1
    Explanation: No number of moves will make the board solved.

Example 3:    
    
    Input: board = [[4,1,2],[5,0,3]]
    Output: 5
    Explanation: 5 is the smallest number of moves that solves the board.

    An example path:

    After move 0: [[4,1,2],[5,0,3]]
    After move 1: [[4,1,2],[0,5,3]]
    After move 2: [[0,1,2],[4,5,3]]
    After move 3: [[1,0,2],[4,5,3]]
    After move 4: [[1,2,0],[4,5,3]]
    After move 5: [[1,2,3],[4,5,0]]

Example 4:    
    
    Input: board = [[3,2,4],[1,5,0]]
    Output: 14

Note:

- board will be a 2 x 3 array as described above.
- board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].

## Method:

bfs, tle:

    class Solution(object):
        def slidingPuzzle(self, board):
            """
            :type board: List[List[int]]
            :rtype: int
            """
            m, n=len(board), len(board[0])
            for i in range(m):
                for j in range(n):
                    if board[i][j]==0:
                        x, y=i, j
                        break
            queue=collections.deque([(x, y, 0, board)])
            s=set()
            while queue:
                x, y, count, board=queue.popleft()
                h=self.hashList(board)
                # if h in s:
                #     return -1
                s.add(h)
                if self.isSolved(board):
                    return count
                for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    if x+dx>=0 and x+dx<m and y+dy>=0 and y+dy<n:
                        board[x][y], board[x+dx][y+dy]=board[x+dx][y+dy], board[x][y]
                        if self.hashList(board) not in s:
                            queue.append((x+dx, y+dy, count+1, board))
                        board[x][y], board[x+dx][y+dy]=board[x+dx][y+dy], board[x][y]
            return -1
                
        def isSolved(self, board):
            m, n=len(board), len(board[0])
            for i in range(m):
                for j in range(n):
                    if board[i][j]!=(i*m+n+1)%6:
                        return False
            return True
        
        def hashList(self, board):
            m, n=len(board), len(board[0])
            return tuple(board[i][j] for i in range(m) for j in range(n))
            
## Solution:

same idea, change matrix to string (hashable):

    class Solution(object):
        def slidingPuzzle(self, board):
            """
            :type board: List[List[int]]
            :rtype: int
            """
            m, n=len(board), len(board[0])
            s=""
            for i in range(m):
                for j in range(n):
                    s+=str(board[i][j])
            queue=collections.deque([(s, 0)])
            seen=set()
            while queue:
                s, count=queue.popleft()
                seen.add(s)
                if s=="123450":
                    return count
                idx=s.index("0")
                for d in [-1, 1, 3, -3]:
                    if idx+d<0 or idx+d>=m*n or (idx==2 and d==1) or (idx==3 and d==-1):
                        continue
                    news=list(s)
                    news[idx], news[idx+d]=news[idx+d], news[idx]
                    news=''.join(news)
                    if news not in seen:
                        queue.append((news, count+1))
            return -1
            
use map to track of index change:

    class Solution(object):
        def slidingPuzzle(self, board):
            """
            :type board: List[List[int]]
            :rtype: int
            """
            m, n=len(board), len(board[0])
            moves={0:[1,3],1:[0,2,4],2:[1,5],3:[0,4],4:[3,5,1],5:[4,2]}
            s=""
            for i in range(m):
                for j in range(n):
                    s+=str(board[i][j])
            queue=collections.deque([(s, s.index("0"), 0)])
            seen=set()
            while queue:
                s, idx, count=queue.popleft()
                seen.add(s)
                if s=="123450":
                    return count
                for d in moves[idx]:
                    news=list(s)
                    news[idx], news[d]=news[d], news[idx]
                    news=''.join(news)
                    if news not in seen:
                        queue.append((news, d, count+1))
            return -1