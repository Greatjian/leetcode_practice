# 047. Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:

    [
      [1,1,2],
      [1,2,1],
      [2,1,1]
    ]
    
## Solution:

类似前题，出现重复元素需加入条件判断删除重复结果。

    class Solution(object):
        def permuteUnique(self, nums):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
            res=[]
            nums.sort()
            return self.getPermute(nums,[],res)
            
        def getPermute(self, nums,path,res):
            for i in range(len(nums)):
                if i>=1 and nums[i]==nums[i-1]:
                    continue
                self.getPermute(nums[:i]+nums[i+1:],path+[nums[i]],res)
            if not nums:
                res.append(path)
            return res
            