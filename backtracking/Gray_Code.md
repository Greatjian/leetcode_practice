# 089. Gray Code

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

    00 - 0
    01 - 1
    11 - 3
    10 - 2
    
Note:
- For a given n, a gray code sequence is not uniquely defined.
- For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.
- For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.

## Methods:
超时，11 / 12 test cases passed。

    class Solution(object):
        def grayCode(self, n):
            """
            :type n: int
            :rtype: List[int]
            """
            if n==0:
                return [0]
            nums=[0 for i in range(n)]
            res=[]
            ans=[]
            self.dfs(nums,res)
            for i in res:
                a=int(''.join(str(e) for e in i),2)
                ans.append(a)
            return ans
            
        def dfs(self,path,res):
            res.append(path[:])
            for i in range(len(path)-1,-1,-1):
                path[i]=1-path[i]
                if path not in res:
                    self.dfs(path,res)
                else:
                    path[i]=1-path[i]
    
## Solution:
位操作：>>右移，^按位异或运算符：当两对应的二进位相异时，结果为1:

    class Solution(object):
        def grayCode(self, n):
            """
            :type n: int
            :rtype: List[int]
            """
            return [i>>1^i for i in range(pow(2,n))]
找规律：
> 0,1 | 3,2     | 6,7,5,4
>
> 0,1 | 1+2,0+2 | 2+4,3+4,1+4,0+4

    class Solution(object):
        def grayCode(self, n):
            """
            :type n: int
            :rtype: List[int]
            """
            if n==0:
                return [0]
            ans=[0,1]
            b=2
            for i in range(n-1):
                for j in range(len(ans)-1,-1,-1):
                    ans.append(ans[j]+b)
                b*=2
            return ans