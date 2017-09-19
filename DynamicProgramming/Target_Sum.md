# 494. Target Sum

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

    Input: nums is [1, 1, 1, 1, 1], S is 3. 
    Output: 5
    Explanation: 
    
    -1+1+1+1+1 = 3
    +1-1+1+1+1 = 3
    +1+1-1+1+1 = 3
    +1+1+1-1+1 = 3
    +1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

Note:
- The length of the given array is positive and will not exceed 20.
- The sum of elements in the given array will not exceed 1000.
- Your output answer is guaranteed to be fitted in a 32-bit integer.

## Method:
dfs超时：

    class Solution(object):
        def findTargetSumWays(self, nums, S):
            """
            :type nums: List[int]
            :type S: int
            :rtype: int
            """
            self.count=0
            self.helper(nums,0,S)
            return self.count
            
        def helper(self, nums, sum, S):
            if not nums:
                if sum==S:
                    self.count+=1
                return
            self.helper(nums[1:],sum+nums[0],S)
            self.helper(nums[1:],sum-nums[0],S)
            
## Solution:
dp counter记录每一次求和出现次数：

    class Solution(object):
        def findTargetSumWays(self, nums, S):
            """
            :type nums: List[int]
            :type S: int
            :rtype: int
            """
            dp = collections.Counter()
            dp[0] = 1
            for n in nums:
                ndp = collections.Counter()
                for k in dp.keys():
                    ndp[k + n] += dp[k]
                    ndp[k - n] += dp[k]
                dp = ndp
            return dp[S]
            
2 * sum(P) = S + sum(nums)
寻找子集和为sum(P)数目：
    
    class Solution(object):
        def findTargetSumWays(self, nums, S):
            """
            :type nums: List[int]
            :type S: int
            :rtype: int
            """
            if (S+sum(nums))%2==1 or sum(nums)<S:
                return 0
            l=(S+sum(nums))/2
            dp=[0]*(l+1)
            dp[0]=1
            for i in range(len(nums)):
                for j in range(l,nums[i]-1,-1):
                    dp[j]+=dp[j-nums[i]]
            return dp[-1]

用dp index记录所有和的情况（长度2*sum(nums)+1）。

因为前元素不能影响后值，每次更新都需要建立新数组再覆盖旧值：

    class Solution(object):
        def findTargetSumWays(self, nums, S):
            """
            :type nums: List[int]
            :type S: int
            :rtype: int
            """
            s = sum(nums) 
            if S>s or S<-s:
                return 0;
            dp = [0]*(2*s+1)
            dp[s] = 1
            for i in range(len(nums)):
                next = [0]*(2*s+1)
                for k in range(2*s+1):
                    if dp[k]!=0:
                        next[k + nums[i]] += dp[k];
                        next[k - nums[i]] += dp[k];
                dp = next;
            return dp[S+s];