# 054. Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

    [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]
You should return [1,2,3,6,9,8,7,4,5].

## Method:
考虑迭代法。

最先的想法是将下一方向优先级依次设置为右下左上，但发现大于4*4矩阵就出错了：

    class Solution(object):
        def spiralOrder(self, matrix):
            """
            :type matrix: List[List[int]]
            :rtype: List[int]
            """
            if not matrix:
                return []
            ans=[matrix[0][0]]
            self.returnNext(matrix,0,0,ans)
            return ans
            
        def returnNext(self,matrix,i,j,ans):
            if j+1<len(matrix[0]) and matrix[i][j+1] not in ans:
                ans.append(matrix[i][j+1])
                self.returnNext(matrix,i,j+1,ans)
                return
            elif i+1<len(matrix)and matrix[i+1][j] not in ans:
                ans.append(matrix[i+1][j])
                self.returnNext(matrix,i+1,j,ans)
                return
            elif j-1>=0 and matrix[i][j-1] not in ans:
                ans.append(matrix[i][j-1])
                self.returnNext(matrix,i,j-1,ans)
                return
            elif i-1>=0 and matrix[i-1][j] not in ans:
                ans.append(matrix[i-1][j])
                self.returnNext(matrix,i-1,j,ans)
                return
            else:
                return

仔细分析发现，下一方向顺序实际与上一次序有关，可单独拿出设置，结果系统表示太复杂了...
>RuntimeError: maximum recursion depth exceeded in cmp


    class Solution(object):
        def spiralOrder(self, matrix):
            """
            :type matrix: List[List[int]]
            :rtype: List[int]
            """
            if not matrix:
                return []
            ans=[matrix[0][0]]
            direction=0
            self.returnNext(matrix,0,0,ans,direction)
            return ans
            
        def returnNext(self,matrix,i,j,ans,direction):
            if direction==0:
                if j+1<len(matrix[0]) and matrix[i][j+1] not in ans:
                    ans.append(matrix[i][j+1])
                    self.returnNext(matrix,i,j+1,ans,direction)
                else:
                    direction=1
                    self.returnNext(matrix,i+1,j,ans,direction)
                return
            if direction==1:
                if i+1<len(matrix)and matrix[i+1][j] not in ans:
                    ans.append(matrix[i+1][j])
                    self.returnNext(matrix,i+1,j,ans,direction)
                else:
                    direction=2
                    self.returnNext(matrix,i,j-1,ans,direction)
                return
            if direction==2:
                if j-1>=0 and matrix[i][j-1] not in ans:
                    ans.append(matrix[i][j-1])
                    self.returnNext(matrix,i,j-1,ans,direction)
                else:
                    direction=3
                    self.returnNext(matrix,i-1,j,ans,direction)
                return
            if direction==3:
                if i-1>=0 and matrix[i-1][j] not in ans:
                    ans.append(matrix[i-1][j])
                    self.returnNext(matrix,i-1,j,ans,direction)
                else:
                    direction=0
                    self.returnNext(matrix,i,j+1,ans,direction)
                return
            else:
                return

## Solution:
事实上，设置direction的思想没有错误，我们没必要要使用递归这么复杂的方式：

    class Solution(object):
        def spiralOrder(self, matrix):
            """
            :type matrix: List[List[int]]
            :rtype: List[int]
            """
            if not matrix:
                return []
            ans=[matrix[0][0]]
            direction=0
            i=j=0
            
            while True:
                if direction==0:
                    if j+1<len(matrix[0]) and matrix[i][j+1] not in ans:
                        ans.append(matrix[i][j+1])
                        j+=1
                    else:
                        direction=1
                        
                if direction==1:
                    if i+1<len(matrix)and matrix[i+1][j] not in ans:
                        ans.append(matrix[i+1][j])
                        i+=1
                    else:
                        direction=2
                        
                if direction==2:
                    if j-1>=0 and matrix[i][j-1] not in ans:
                        ans.append(matrix[i][j-1])
                        j-=1
                    else:
                        direction=3
                        
                if direction==3:
                    if i-1>=0 and matrix[i-1][j] not in ans:
                        ans.append(matrix[i-1][j])
                        i-=1
                    else:
                        direction=0
                        
                if len(ans)==len(matrix)*len(matrix[0]):
                    break
                
            return ans
            
优秀答案共欣赏：

循环判断用总元素数=矩阵长乘宽，拐点判断用%边长余数。

    class Solution(object):
        def spiralOrder(self, matrix):
            """
            :type matrix: List[List[int]]
            :rtype: List[int]
            """
            res = []
            if not matrix:
                return res
            i, j, di, dj = 0, 0, 0, 1
            m, n = len(matrix), len(matrix[0])
            for v in range(m*n):
                res.append(matrix[i][j])
                matrix[i][j] = ""
                if matrix[(i+di)%m][(j+dj)%n] == "":
                    di, dj = dj, -di
                i += di
                j += dj
            return res