# 238. Product of Array Except Self

Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

    For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

## Method:
直接法，超时：

    class Solution(object):
        def productExceptSelf(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            res=[]
            for i in range(len(nums)):
                res.append(self.getProduct(nums[:i]+nums[i+1:]))
            return res
                               
        def getProduct(self, nums):
            product=1
            for num in nums:
                product*=num
            return product
## Solution:
设置新数组，正反各遍历数组一遍：

>nums:[a,b,c,d]
>
>res:[1, a, a*b, a*b*c]
>
>res:[b*c*d,a*c*d,a*b*d,a*b*c]

    class Solution(object):
        def productExceptSelf(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            res = [1] * len(nums)
            acc = 1
            for i in xrange(len(nums)):
                res[i] = acc
                acc *= nums[i]
                
            acc = 1
            for i in xrange(len(nums) - 1, -1, -1):
                res[i] *= acc
                acc *= nums[i]
                
            return res
            
