# 090 Subsets II


Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

    [
      [2],
      [1],
      [1,2,2],
      [2,2],
      [1,2],
      []
    ]

## Method:
可先试用subsets I方法，后删除列表中重复元素：

    class Solution(object):
        def subsetsWithDup(self, nums):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
            res = [[]]
            nums.sort()
            for num in nums:
                res += [[num] + i for i in res]
            count = 1
            res.sort()
            for i in range(1, len(res)):
                if res[i] != res[i - 1]:
                    res[count] = res[i]
                    count += 1
            return res[:count]

## Solution:
若新添加元素与之前不同，则新元素分别于结果中所有元素结合添加；否则与上一添加结果后元素结合添加：

    class Solution(object):
        def subsetsWithDup(self, nums):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
            nums.sort()
            output = [[]]
            cnt = 1
            for i in range(len(nums)):
                j = 0
                if i > 0 and nums[i] == nums[i-1]:
                    j = cnt
                cnt = len(output)
                for k in range(j, cnt):
                    t = output[k]
                    output.append(t + [nums[i]])
            return output
自己创作：
            
    class Solution(object):
        def subsetsWithDup(self, nums):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
            res = [[]]
            nums.sort()
            for i in range(len(nums)):
                j=0
                if i>0 and nums[i]==nums[i-1]:
                    j=start
                start=len(res)
                for k in range(j,start):
                    res.append([nums[i]]+res[k])
            return res
最佳recursion method:
    
    class Solution(object):
        def subsetsWithDup(self, nums):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
            nums.sort()
            res = []
            return self.getSubset(nums,[],res)
        
        def getSubset(self,nums,path,res):
            res.append(path)
            for i in range(len(nums)):
                if i-1>=0 and nums[i]==nums[i-1]:
                    continue
                self.getSubset(nums[i+1:],path+[nums[i]],res)
            return res