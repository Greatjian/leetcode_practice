# 152. Maximum Product Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

## Method:
最大值最小值分别为前任最大最小与新数相乘以及新数本身比较的最大最小：

比较时要注意maxp中段会改变数值，故需要提前赋值给新变量。

    class Solution(object):
        def maxProduct(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            res=maxp=maxn=nums[0]
            for i in range(1,len(nums)):
                positive=maxp
                maxp=max(positive*nums[i],maxn*nums[i],nums[i])
                maxn=min(positive*nums[i],maxn*nums[i],nums[i])
                res=max(res,maxp)
            return res
            
## Solution:
当然，我们可根据新数正负，对于最大最小做出更简单的判断比较：

    class Solution(object):
        def maxProduct(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            res=maxp=maxn=nums[0]
            for i in range(1,len(nums)):
                if nums[i]<0:
                    maxp,maxn=maxn,maxp
                maxp=max(maxp*nums[i],nums[i])
                maxn=min(maxn*nums[i],nums[i])
                res=max(res,maxp)
            return res