# 077. Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

    [
      [2,4],
      [3,4],
      [2,3],
      [1,2],
      [1,3],
      [1,4],
    ]

## Method:
超时（26 / 27 test cases passed）：

    class Solution(object):
        def combine(self, n, k):
            """
            :type n: int
            :type k: int
            :rtype: List[List[int]]
            """
            res=[]
            nums=[i for i in range(1,n+1)]
            self.dfs(nums,[],k,res)
            return res
            
        def dfs(self,nums,path,k,res):
            if len(path)==k:
                res.append(path)
                return
            for i in range(len(nums)):
                self.dfs(nums[i+1:], path+[nums[i]],k,res)
## Solution:
加一条判断语句，可去除不必要的dfs：

    class Solution(object):
        def combine(self, n, k):
            """
            :type n: int
            :type k: int
            :rtype: List[List[int]]
            """
            res=[]
            nums=[i for i in range(1,n+1)]
            self.dfs(nums,[],k,res)
            return res
            
        def dfs(self,nums,path,k,res):
            if len(path)==k:
                res.append(path)
                return
            for i in range(len(nums)):
                if len(path)+len(nums)-i>=k:
                    self.dfs(nums[i+1:], path+[nums[i]],k,res)

另一种思路，直接在主函数自我调用：

    class Solution(object):
        def combine(self, n, k):
            """
            :type n: int
            :type k: int
            :rtype: List[List[int]]
            """
            if k <= 0 or n <= 0:
                return [[]]
            if k == n:
                return [[x for x in range(1,n+1)]]
            if k > n:
                return []
            return [[n]+x for x in self.combine(n-1, k-1)] + [x for x in self.combine(n-1, k)]