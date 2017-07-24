# 079. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

    [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]
word = "ABCCED", -> returns true,

word = "SEE", -> returns true,

word = "ABCB", -> returns false.

## Method:
使用尾递归：

    import copy
    class Solution(object):
        def exist(self, board, word):
            firstwords=[]
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == word[0]:
                        firstwords.append([i,j])
            if firstwords==[]:
                return False
            print(firstwords)
    
            boards=copy.deepcopy(board)
    
            for firstword in firstwords:
                for i in range(len(board)):
                    for j in range(len(board[0])):
                        board[i][j]=boards[i][j]
                # board=boards则不行？
                if self.search(board, word, 1, firstword[0], firstword[1])==True:
                    return True
            return False
    
        def search(self, board, word, start, i, j):
            board[i][j] = 'None'
            while start < len(word):
                if i + 1 < len(board) and board[i + 1][j] == word[start]:
                    return self.search(board, word, start + 1, i+1, j)
                elif i - 1 >= 0 and board[i - 1][j] == word[start]:
                    return self.search(board, word, start + 1, i-1, j)
                elif j + 1 < len(board[0]) and board[i][j + 1] == word[start]:
                    return self.search(board, word, start + 1, i, j+1)
                elif j - 1 >= 0 and board[i][j-1] == word[start]:
                    return self.search(board, word, start + 1, i, j-1)
                else:
                    print(board)
                    return False
            return True
    
    x=Solution()
    print(x.exist([['C','A','A'],
                   ['A','A','A'],
                   ['B','C','D']]
    ,"AAB"))    
但错误之处在于同一点下方向可能有多种选择，if语句只能选择其中之一。

如何改进？

可以在判断时直接返回结果，但若返回失败需在函数内部重置该元素值，代码如下：

    import copy
    class Solution(object):
        def exist(self, board, word):
            firstwords=[]
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == word[0]:
                        firstwords.append([i,j])
            if firstwords==[]:
                return False
            print(firstwords)
    
            boards=copy.deepcopy(board)
    
            for firstword in firstwords:
                for i in range(len(board)):
                    for j in range(len(board[0])):
                        board[i][j]=boards[i][j]
                if self.search(board, word, 1, firstword[0], firstword[1])==True:
                    return True
            return False
    
        def search(self, board, word, start, i, j):
            board[i][j] = 'None'
            while start < len(word):
                if i + 1 < len(board) and board[i + 1][j] == word[start] and self.search(board, word, start + 1, i+1, j):
                    return True
                elif i - 1 >= 0 and board[i - 1][j] == word[start] and self.search(board, word, start + 1, i-1, j):
                    return True
                elif j + 1 < len(board[0]) and board[i][j + 1] == word[start] and self.search(board, word, start + 1, i, j+1):
                    return True
                elif j - 1 >= 0 and board[i][j-1] == word[start] and self.search(board, word, start + 1, i, j-1):
                    return True
                else:
                    board[i][j] =word[start-1]
                    print(board)
                    return False
            return True
    
    x=Solution()
    print(x.exist([['C','A','A'],
                   ['A','A','A'],
                   ['B','C','D']]
    ,"CAAAAA"))

由于忽略了此时外部函数deepcopy更新已无意义，导致运行时间过长...

![](/pic/%20long_time_code_submission.jpeg)

删除无用代码后，新代码如下：

    class Solution(object):
        def exist(self, board, word):
            """
            :type board: List[List[str]]
            :type word: str
            :rtype: bool
            """
            firstwords=[]
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == word[0]:
                        firstwords.append([i,j])
            if firstwords==[]:
                return False
            print(firstwords)
    
            for firstword in firstwords:
                if self.search(board, word, 1, firstword[0], firstword[1])==True:
                    return True
            return False
    
        def search(self, board, word, start, i, j):
            board[i][j] = 'None'
            while start < len(word):
                if i + 1 < len(board) and board[i + 1][j] == word[start] and self.search(board, word, start + 1, i+1, j):
                    return True
                elif i - 1 >= 0 and board[i - 1][j] == word[start] and self.search(board, word, start + 1, i-1, j):
                    return True
                elif j + 1 < len(board[0]) and board[i][j + 1] == word[start] and self.search(board, word, start + 1, i, j+1):
                    return True
                elif j - 1 >= 0 and board[i][j-1] == word[start] and self.search(board, word, start + 1, i, j-1):
                    return True
                else:
                    board[i][j] =word[start-1]
                    return False
            return True
运行速度如下：

![](/pic/%20regular_time_code_submission.jpeg)

效果拔群，说明思路是正确的，不过和后面答案比较还有进步的空间。

## Solution:
相比之下的优点：

直接从首位判断，省略firstwords一步；

判断标识不改变矩阵本身，而是在每个点设置visited True/False值判断，省略deepcopy步骤；

    class Solution:
        # @param board, a list of lists of 1 length string
        # @param word, a string
        # @return a boolean
        def exist(self, board, word):
            # write your code here
            # Boundary Condition
            if word == []:
                return True
            m = len(board)
            if m == 0:
                return False
            n = len(board[0])
            if n == 0:
                return False
            # Visited Matrix
            visited = [[False for j in range(n)] for i in range(m)]
            # DFS
            for i in range(m):
                for j in range(n):
                    if self.exist2(board, word, visited, i, j):
                        return True
            return False
    
        def exist2(self, board, word, visited, row, col):
            if word == '':
                return True
            m, n = len(board), len(board[0])
            if row < 0 or row >= m or col < 0 or col >= n:
                return False
            if board[row][col] == word[0] and not visited[row][col]:
                visited[row][col] = True
                # row - 1, col
                if self.exist2(board, word[1:], visited, row - 1, col) or self.exist2(board, word[1:], visited, row, col - 1) or self.exist2(board, word[1:], visited, row + 1, col) or self.exist2(board, word[1:], visited, row, col + 1):
                    return True
                else:
                    visited[row][col] = False
            return False
另一种方法（判断时直接返回结果，未使用visited T/F值减少空间消耗，但处理时改变矩阵元素数值，
比较tricky）：
    
    class Solution(object):
        def exist(self, board, word):
            """
            :type board: List[List[str]]
            :type word: str
            :rtype: bool
            """
            
            length = len(board)
            if length == 0:
                return False
            rowlength = len(board[0])
            end = len(word)
            
            
            def walk(a, b, i):
                if board[a][b] != word[i]:
                    return False
                elif i == end - 1:
                    return True
                else:
                    board[a][b] = None
                    if a>0 and board[a-1][b] and walk(a-1, b, i+1):
                        return True
                    if a + 1 < length and board[a+1][b] and walk(a+1, b, i+1):
                        return True
                    if b > 0 and board[a][b - 1] and walk(a, b-1, i+1):
                        return True
                    if b + 1 < rowlength and board[a][b + 1] and walk(a, b+1, i+1):
                        return True
                    board[a][b] = word[i]    
                    return False
                    
            
            for i in range(length):
                for j in range(rowlength):
                    if walk(i, j, 0):
                        return True
            
            return False
