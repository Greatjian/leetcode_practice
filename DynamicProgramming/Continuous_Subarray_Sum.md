# 523. Continuous Subarray Sum

Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:

    Input: [23, 2, 4, 6, 7],  k=6
    Output: True
    Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.

Example 2:

    Input: [23, 2, 6, 4, 7],  k=6
    Output: True
    Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.

Note:

- The length of the array won't exceed 10,000.
- You may assume the sum of all the numbers is in the range of a signed 32-bit integer.

## Method:
建立二维dp数组遍历，超时：

    class Solution(object):
        def checkSubarraySum(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: bool
            """
            l=len(nums)
            dp=[[-1]*l for _ in range(l)]
            for i in range(l):
                dp[i][0]=nums[i]
                for j in range(1,i+1):
                    dp[i][j]=dp[i][0]+dp[i-1][j-1]
                    if k==0:
                        if dp[i][j]==0:
                            return True
                    elif dp[i][j]%k==0:
                        return True
            return False
            
## Solution:
subarray sum可转化为任意两Index总和之差，后利用相同模且index差大于一做判断：

    class Solution(object):
        def checkSubarraySum(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: bool
            """
            d={0:-1}
            tot=0
            for i,s in enumerate(nums):
                tot+=s
                m=tot%k if k else tot
                if m not in d:
                    d[m]=i
                elif d[m]+1<i:
                    return True
            return False