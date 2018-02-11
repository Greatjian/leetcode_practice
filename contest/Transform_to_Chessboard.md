# 782. Transform to Chessboard

An N x N board contains only 0s and 1s. In each move, you can swap any 2 rows with each other, or any 2 columns with each other.

What is the minimum number of moves to transform the board into a "chessboard" - a board where no 0s and no 1s are 4-directionally adjacent? If the task is impossible, return -1.

    Examples:
    Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
    Output: 2
    
    Explanation:
    One potential sequence of moves is shown below, from left to right:
    
    0110     1010     1010
    0110 --> 1010 --> 0101
    1001     0101     1010
    1001     0101     0101
    
    The first move swaps the first and second column.
    The second move swaps the second and third row.
    
    
    Input: board = [[0, 1], [1, 0]]
    Output: 0
    
    Explanation:
    Also note that the board with 0 in the top left corner,
    01
    10
    
    is also a valid chessboard.
    
    Input: board = [[1, 0], [1, 0]]
    Output: -1
    
    Explanation:
    No matter what sequence of moves you make, you cannot end with a valid chessboard.

Note:

- board will have the same number of rows and columns, a number in the range [2, 30].
- board[i][j] will be only 0s or 1s.

## Method:

bfs+memo, change to string, tle:

O(n^4)

    class Solution(object):
        def movesToChessboard(self, board):
            """
            :type board: List[List[int]]
            :rtype: int
            """
            n=len(board)
            string=''
            for i in range(n):
                for j in range(n):
                    string+=str(board[i][j])
            if not n%2:
                target=[('01'*(n/2)+'10'*(n/2))*(n/2), ('10'*(n/2)+'01'*(n/2))*(n/2)]
            else:
                target=[('01'*(n/2)+'0'+'10'*(n/2)+'1')*(n/2)+'01'*(n/2)+'0', ('10'*(n/2)+'1'+'01'*(n/2)+'0')*(n/2)+'10'*(n/2)+'1']
            queue=collections.deque([string])
            res=0
            s=set([string])
            while queue:
                for _ in range(len(queue)):
                    node=queue.popleft()
                    if node in target:
                        return res
                    for news in self.transform(node):
                        if news not in s:
                            s.add(news)
                            queue.append(news)
                res+=1
            return -1
                    
        def transform(self, s):
            l=int(len(s)**0.5)
            res=[]
            for i in range(l):
                for j in range(i+1, l):
                    res.append(s[:i*l]+s[j*l:(j+1)*l]+s[(i+1)*l:j*l]+s[i*l:(i+1)*l]+s[(j+1)*l:])
            for mod1 in range(l):
                for mod2 in range(mod1+1, l):
                    news=list(s)
                    for i in range(l):
                        news[i*l+mod1], news[i*l+mod2]=news[i*l+mod2], news[i*l+mod1]
                    res.append(''.join(news))
            return res
            
## Solution:

two cases for each row and column, compare and add, O(n^2):

    class Solution(object):
        def movesToChessboard(self, board):
            """
            :type board: List[List[int]]
            :rtype: int
            """
            n=len(board)
            for s in [set(zip(*board)), set(map(tuple, board))]:
                if len(s)!=2:
                    return -1
                if n%2==0:
                    for i in s:
                        if sum(i)!=n/2:
                            return -1
                if n%2:
                    for i in s:
                        if sum(i) not in [n/2, n/2+1]:
                            return -1
            count=0
            for i in [board[0], zip(*board)[0]]:
                if n%2==0:
                    p=0
                    cnt1, cnt2=0, 0
                    for j in i:
                        cnt1+=j^p
                        cnt2+=j^(1-p)
                        p=1-p
                    count+=min(cnt1, cnt2)/2
                else:
                    cnt=0
                    p=(0 if sum(i)==n/2 else 1)
                    for j in i:
                        cnt+=j^p
                        p=1-p
                    count+=cnt/2
            return count