# 060. Permutation Sequence

The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"
    
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.

## Method:
超时，不必跑出所有结果（37 / 200 test cases passed）：

    class Solution(object):
        def getPermutation(self, n, k):
            """
            :type n: int
            :type k: int
            :rtype: str
            """
            nums=[i for i in range(1,n+1)]
            res=[]
            self.dfs(nums, '', res)
            return res[k-1]
            
        
        def dfs(self, nums, path, res):
            if not nums:
                res.append(path)
                return
            for i in range(len(nums)):
                self.dfs(nums[:i]+nums[i+1:], path+str(nums[i]), res)

有进步，但还是超时（53 / 200 test cases passed）：

    class Solution(object):
        def getPermutation(self, n, k):
            """
            :type n: int
            :type k: int
            :rtype: str
            """
            nums=[i for i in range(1,n+1)]
            res=[]
            self.dfs(nums, '', res, k)
            return res[k-1]
            
        
        def dfs(self, nums, path, res, k):
            if not nums:
                res.append(path)
            if len(res)==k:
                return
            for i in range(len(nums)):
                self.dfs(nums[:i]+nums[i+1:], path+str(nums[i]), res, k)

## Solution:
使用n-1阶乘迭代：

    class Solution(object):
        def getPermutation(self, n, k):
            """
            :type n: int
            :type k: int
            :rtype: str
            """
            res=[]
            k-=1
            nums=[i for i in range(1,n+1)]
            self.dfs(nums, '', k, res)
            return ''.join(res)
            
        
        def dfs(self, nums, path, k, res):
            n=len(nums)
            if not nums:
                res.append(path)
                return
            a=k/self.getFactorial(n-1)
            self.dfs(nums[:a]+nums[a+1:],path+str(nums[a]), k%self.getFactorial(n-1), res)
                
        def getFactorial(self, n):
            if n==0:
                return 1
            factorial=1
            for i in range(1,n+1):
                factorial*=i
            return factorial         
               
factorial可直接引用math:

    class Solution(object):
        def getPermutation(self, n, k):
            """
            :type n: int
            :type k: int
            :rtype: str
            """
            res=[]
            k-=1
            nums=[i for i in range(1,n+1)]
            self.dfs(nums, '', k, res)
            return ''.join(res)
            
        
        def dfs(self, nums, path, k, res):
            n=len(nums)
            if not nums:
                res.append(path)
                return
            a=k/math.factorial(n-1)
            self.dfs(nums[:a]+nums[a+1:],path+str(nums[a]), k%math.factorial(n-1), res)