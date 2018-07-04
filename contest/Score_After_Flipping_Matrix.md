# 861. Score After Flipping Matrix

We have a two dimensional matrix A where each value is 0 or 1.

A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.

After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score.

 

Example 1:

    Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
    Output: 39
    Explanation:
    Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
    0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
 

Note:

- 1 <= A.length <= 20
- 1 <= A[0].length <= 20
- A[i][j] is 0 or 1.

## Method:

build the first line of matrix, then the rest, finally calculate: 

    class Solution(object):
        def matrixScore(self, A):
            """
            :type A: List[List[int]]
            :rtype: int
            """
            m, n =len(A), len(A[0])
            for i in range(m):
                if A[i][0]==0:
                    for j in range(n):
                        A[i][j]=1-A[i][j]
            for j in range(1, n):
                one=sum(1 for i in range(m) if A[i][j]==1)
                zero=sum(1 for i in range(m) if A[i][j]==0)
                if zero>one:
                    for i in range(m):
                        A[i][j]=1-A[i][j]
            res=0
            for i in range(m):
                tmp=0
                for j in range(n):
                    tmp=tmp*2+A[i][j]
                res+=tmp
            return res
                    