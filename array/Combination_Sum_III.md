# 216. Combination Sum III

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


Example 1:

    Input: k = 3, n = 7

Output:

    [[1,2,4]]

Example 2:

    Input: k = 3, n = 9

Output:

    [[1,2,6], [1,3,5], [2,3,4]]
    
## Solution:
模仿前两题：

    class Solution(object):
        def combinationSum3(self, k, n):
            """
            :type k: int
            :type n: int
            :rtype: List[List[int]]
            """
            nums=[1,2,3,4,5,6,7,8,9]
            res=[]
            return self.getCombination(nums,n,[],k,res)
        
        def getCombination(self,nums,n,path,k,res):
            if n==0 and k==0:
                res.append(path)
            for i in range(len(nums)):
                if nums[i]<=n:
                    self.getCombination(nums[i+1:],n-nums[i],path+[nums[i]],k-1,res)
            return res
            