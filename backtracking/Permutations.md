# 046. Permutations

Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:

    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]
## Method:

    class Solution(object):
        def permute(self, nums):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
            res=[]
            return self.getPermutation(nums,[],res)
            
        def getPermutation(self, nums, current, res):
            for i in range(len(nums)):
                current.append(nums[i])
                self.getPermutation(nums[:i]+nums[i+1:],current,res)
                current.pop()
            if not nums:
                res.append(current[:])
            return res
两点疑问：
- 为何res.append时需要对current进行复制？（直接append current会return为空集）
- 前后回溯时每一层nums与current的取值？（current变化而nums未变化）

![](/pic/q.jpeg)

## Solution:

    class Solution(object):
        def permute(self, nums):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
            res=[]
            return self.getPermutation(nums,[],res)
            
        def getPermutation(self, nums, current, res):
            for i in range(len(nums)):
                self.getPermutation(nums[:i]+nums[i+1:],current+[nums[i]],res)
            if not nums:
                res.append(current)
            return res
                
            
            