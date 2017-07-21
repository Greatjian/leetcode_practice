# 053. Maximum Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
If you have figured out the O(n) solution, 
try coding another solution using the divide and conquer approach,
which is more subtle.

## Method:
最先想到暴力法O(n^2)，超时。

    class Solution(object):
        def maxSubArray(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            maxi=max(nums)
            for i in range(len(nums)-1):
                sum=nums[i]
                maxi= max(sum,maxi)
                for j in range(i+1,len(nums)):
                    sum+=nums[j]
                    maxi=max(sum,maxi)
            return maxi

## Solution:
动态规划问题的考量：遍历数组分别考虑任何一元素作为起点，
初始值为之前累积的最大值与0之间的最大值。

```
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_history = current = nums[0]
        for item in nums[1:]:
            current = max(item, item+ current)
            max_history = max(current, max_history)
        return max_history
```

```
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=current=nums[0]
        for i in range(1,len(nums)):
            current=max(0,current)
            current+=nums[i]
            m=max(m,current)
        return m
```