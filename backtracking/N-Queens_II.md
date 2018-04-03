# 052. N-Queens II

Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.

## Method:

    class Solution(object):
        def totalNQueens(self, n):
            """
            :type n: int
            :rtype: int
            """
            self.cnt=0
            self.dfs(n, [], [], [], 0)
            return self.cnt
        
        def dfs(self, n, a, b, c, idx):
            if idx==n:
                self.cnt+=1
                return
            for i in range(n):
                if i not in a and i+idx not in b and i-idx not in c:
                    self.dfs(n, a+[i], b+[i+idx], c+[i-idx], idx+1)
            