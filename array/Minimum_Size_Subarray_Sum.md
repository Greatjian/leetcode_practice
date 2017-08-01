# 209. Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

More practice:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

## Method:
双指针操作：右侧指针右移，和超过s后左指针左移，和小于s后右指针右移，
以此类推直到遍历完全部数组：

    class Solution(object):
        def minSubArrayLen(self, s, nums):
            """
            :type s: int
            :type nums: List[int]
            :rtype: int
            """
            if not nums:
                return 0
            sum=0
            ans=len(nums)+1
            left=right=0
            while right<len(nums):
                while True:
                    sum+=nums[right]
                    right+=1
                    if sum>=s:
                        break
                    if sum<s and right==len(nums):
                        return 0 if ans>len(nums) else ans
                while sum>=s:   
                    sum-=nums[left]
                    left+=1
                ans=min(ans,right-left+1)
            return ans
## Solution:
同样的思路可以有更直观简洁的代码：

    class Solution(object):
        def minSubArrayLen(self, s, nums):
            """
            :type s: int
            :type nums: List[int]
            :rtype: int
            """
    
            n = len(nums)
            #if n == 0:
            #    return 0
            left, right = 0, 0
            minLen = n+1
            sumCur = 0
            
            while (right < n):
                while sumCur < s and right < n:
                     sumCur += nums[right]
                     right +=1
                     
                while sumCur >= s:
                    minLen = min(minLen, right - left)
                    sumCur -= nums[left]
                    left+=1
                    
            return 0 if minLen==n+1 else minLen
或：

    class Solution(object):
        def minSubArrayLen(self, s, nums):
            """
            :type s: int
            :type nums: List[int]
            :rtype: int
            """
            sm=-1
            total=0
            left=0
            result=len(nums)+1
            for right, n in enumerate(nums):
                total+=n
                while total>=s:
                    result=min(result,right-left+1)
                    total-=nums[left]
                    left+=1
            if result<=len(nums):
                return result
            else:
                return 0