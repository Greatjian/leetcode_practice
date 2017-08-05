# 560. Subarray Sum Equals K

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

    Input:nums = [1,1,1], k = 2
    Output: 2

Note:
- The length of the array is in range [1, 20,000].
- The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

## Method:
双指针，复杂度O(n2)超时：

    class Solution(object):
        def subarraySum(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: int
            """
            s=count=0
            for l in range(len(nums)):
                r=l
                while r<len(nums):
                    s=s+nums[r]
                    r+=1
                    if s==k:
                        count+=1
                    if r==len(nums):
                        s=0
                        break
            return count
            
使用dict计数，sum(j)-sum(i)=k，但k=0情况需要单独考虑：

    class Solution(object):
        def subarraySum(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: int
            """
            ans = sums = 0
            cnt = collections.Counter()
            for num in nums:
                sums+=num
                cnt[sums] += 1
                if sums==k:
                    ans+=1
                if k!=0:
                    ans+=cnt[sums-k]
            if k==0:
                for element in cnt:
                    if cnt[element]>0:
                        ans+=cnt[element]*(cnt[element]-1)/2
            return ans
                  
## Solution:
添加cnt[0]=1，通过错位循环解决k=0情况：

    class Solution(object):
        def subarraySum(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: int
            """
            ans = sums = 0
            cnt = collections.Counter()
            for num in nums:
                cnt[sums] += 1
                sums += num
                ans += cnt[sums - k]
            return ans

    
            