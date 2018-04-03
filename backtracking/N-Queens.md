# 051. N-Queens

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,

    There exist two distinct solutions to the 4-queens puzzle:
    
    [
     [".Q..",  // Solution 1
      "...Q",
      "Q...",
      "..Q."],
    
     ["..Q.",  // Solution 2
      "Q...",
      "...Q",
      ".Q.."]
    ]

## Method:

    class Solution(object):
        def solveNQueens(self, n):
            """
            :type n: int
            :rtype: List[List[str]]
            """
            
            def dfs(a, b, c, res, idx):
                if idx==n:
                    res.append(a)
                    return
                for i in range(n):
                    if i not in a and i+idx not in b and i-idx not in c:
                        dfs(a+[i], b+[i+idx], c+[i-idx], res, idx+1)
                        
            def convert(l):
                res=[['.']*n for _ in range(n)]
                for i in range(n):
                    res[i][l[i]]="Q"
                    res[i]=''.join(j for j in res[i])
                return res
            
            res=[]
            dfs([], [], [], res, 0)
            return map(convert, res)

          # return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in res]