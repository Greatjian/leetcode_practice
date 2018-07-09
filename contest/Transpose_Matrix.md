# 868. Transpose Matrix

Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

 

    Example 1:
    
    Input: [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[1,4,7],[2,5,8],[3,6,9]]
    
    Example 2:
    
    Input: [[1,2,3],[4,5,6]]
    Output: [[1,4],[2,5],[3,6]]
 

Note:

- 1 <= A.length <= 1000
- 1 <= A[0].length <= 1000

## Method:

    class Solution(object):
        def transpose(self, A):
            """
            :type A: List[List[int]]
            :rtype: List[List[int]]
            """
            m, n=len(A), len(A[0])
            res=[[0]* m for _ in range(n)]
            for i in range(m):
                for j in range(n):
                    res[j][i]=A[i][j]
            return res