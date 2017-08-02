# 078. Subsets

Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]
## Method:
iteration method:

    class Solution(object):
        def subsets(self, nums):
            res = [[]]
            for num in nums:
                res += [item + [num] for item in res]
            return res

recursion method:
            
    class Solution(object):
        def subsets(self, nums):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
            res = []
            self.dfs(sorted(nums), 0, [], res)
            return res
        
        def dfs(self, nums, index, path, res):
            res.append(path)
            for i in xrange(index, len(nums)):
                self.dfs(nums, i + 1, path + [nums[i]], res)
                

[]---1---12---123
      
[]---1---13
      
[]---2---23
  
[]---3

## Solution:

    class Solution(object):
        def subsets(self, nums):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """ 
            res=[]
            return self.dfs(nums,[],res)
            
        def dfs(self,nums,path,res):
            res.append(path)
            for i in range(len(nums)):
                self.dfs(nums[i+1:],path+[nums[i]],res)
            return res