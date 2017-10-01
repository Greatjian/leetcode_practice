# 673. Number of Longest Increasing Subsequence

Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:

    Input: [1,3,5,4,7]
    Output: 2
    
    Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:

    Input: [2,2,2,2,2]
    Output: 5
    
    Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.

## Method:
建立两个dp list，分别记录数值和数量：

    class Solution(object):
        def findNumberOfLIS(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            ans=0
            dp=[1]*len(nums)
            count=[1]*len(nums)
            for i in range(len(nums)):
                for j in range(i):
                    if nums[i]>nums[j]:
                        if dp[j]+1==dp[i]:
                            count[i]+=count[j]
                        if dp[j]+1>dp[i]:
                            dp[i]=dp[j]+1
                            count[i]=count[j]
            for i in range(len(dp)):
                if dp[i]==max(dp):
                    ans+=count[i]
            return ans

最后一部分还可以这样写：

    return sum(y for x,y in zip(dp,count) if x==max(dp))

                        