# 300. Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,

    Given [10, 9, 2, 5, 3, 7, 101, 18],
    The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

## Method:

O(n*n): dp状态转移方程：dp[x] = max(dp[x], dp[y] + 1) 其中 y < x 并且 nums[x] > nums[y]

    class Solution(object):
        def lengthOfLIS(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            dp=[1]*len(nums)
            for i in range(len(nums)):
                for j in range(i):
                    if nums[i]>nums[j]:
                        dp[i]=max(dp[i],dp[j]+1)
            return max(dp) if dp else 0
## Solution:
nlogn:二分法

[1,3,6,7,9,4,10,5,6]

[1]

[1, 3]

[1, 3, 6]

[1, 3, 6, 7]

[1, 3, 6, 7, 9]

[1, 3, 4, 7, 9]

[1, 3, 4, 7, 9, 10]

[1, 3, 4, 5, 9, 10]

[1, 3, 4, 5, 6, 10]


    class Solution(object):
        def lengthOfLIS(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            size = len(nums)
            dp = []
            for x in range(size):
                low, high = 0, len(dp) - 1
                while low <= high:
                    mid = (low + high) / 2
                    if dp[mid] >= nums[x]:
                        high = mid - 1
                    else:
                        low = mid + 1
                if low >= len(dp):
                    dp.append(nums[x])
                else:
                    dp[low] = nums[x]
            return len(dp)