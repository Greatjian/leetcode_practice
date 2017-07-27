# 118. Pascal's Triangle

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

    [
         [1],
        [1,1],
       [1,2,1],
      [1,3,3,1],
     [1,4,6,4,1]
    ]
    
## Solution:
找规律，从第三行开始遍历：

    class Solution(object):
        def generate(self, numRows):
            """
            :type numRows: int
            :rtype: List[List[int]]
            """
            if not numRows:
                return []
            if numRows==1:
                return [[1]]
            if numRows==2:
                return [[1],[1,1]]
            res=[[1],[1,1]]
            for n in range(2,numRows):
                res.append([1]+[res[-1][j]+res[-1][j+1] for j in range(n-1)]+[1])
                # res.append([1]+[a+b for (a,b) in zip(res[-1][1:],res[-1][:-1])]+[1])
            return res