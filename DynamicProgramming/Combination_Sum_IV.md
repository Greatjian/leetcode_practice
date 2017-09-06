# 377. Combination Sum IV

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

    nums = [1, 2, 3]
    target = 4
    
    The possible combination ways are:
    (1, 1, 1, 1)
    (1, 1, 2)
    (1, 2, 1)
    (1, 3)
    (2, 1, 1)
    (2, 2)
    (3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.

Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

## Method:
backtracking: Time Limit Exceeded.

    class Solution(object):
        def combinationSum4(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: int
            """
            ans=[]
            self.getSum(nums, target,[],ans)
            return len(ans)
            
        def getSum(self, nums, target, path, ans):
            if target==0:
                ans.append(path)
                return
            for i in range(len(nums)):
                if target-nums[i]>=0:
                    self.getSum(nums, target-nums[i], path+[nums[i]],ans)
      
减少空间储存，但时间不变，依旧超时：

    class Solution(object):
        def combinationSum4(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: int
            """
            self.count=0
            
            def getSum(nums, target):
                if target==0:
                    self.count+=1
                    return
                for i in range(len(nums)):
                    if target-nums[i]>=0:
                        getSum(nums, target-nums[i])
                        
            getSum(nums, target)
            return self.count
            
backtracking type 3 超时：

    class Solution(object):
        def combinationSum4(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: int
            """
            if target==0:
                return 1
            res=0
            for i in range(len(nums)):
                if target-nums[i]>=0:
                    res+=self.combinationSum4(nums, target-nums[i])
            return res
            
## Solution:
dp，其中dp[x]表示生成数字x的所有可能的组合方式的个数：

    class Solution(object):
        def combinationSum4(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: int
            """
            dp = [0] * (target + 1)
            dp[0] = 1
            for x in range(target + 1):
                for y in nums:
                    if x + y <= target:
                        dp[x + y] += dp[x]
            return dp[-1]