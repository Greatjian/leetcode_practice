# 059. Spiral Matrix II

Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
    
    [
     [ 1, 2, 3 ],
     [ 8, 9, 4 ],
     [ 7, 6, 5 ]
    ]
    
## Method:
参考spiral matrix 1的优秀解法，实现代码如下：

学会二维数组的一步建立。

    class Solution(object):
        def generateMatrix(self, n):
            """
            :type n: int
            :rtype: List[List[int]]
            """
            list = [[0 for i in range(n)] for j in range(n)]
            m=1
            i,j,di,dj=0,0,0,1
            for count in range(n*n):
                list[i][j]=m
                m+=1
                if list[(i+di)%n][(j+dj)%n]!=0:
                    di,dj=dj,-di
                i+=di
                j+=dj
            return list
            