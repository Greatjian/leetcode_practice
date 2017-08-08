# 628. Maximum Product of Three Numbers

Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:

    Input: [1,2,3]
    Output: 6

Example 2:

    Input: [1,2,3,4]
    Output: 24

Note:
- The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
- Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

## Method:
最大三数和为数组最大三数乘积或最大数乘两最小数值：

    class Solution(object):
        def maximumProduct(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            nums.sort()
            l1,l2,l3,s1,s2=-1,-2,-3,0,1
            return max(nums[l1]*nums[l2]*nums[l3],nums[l1]*nums[s1]*nums[s2])

## Solution:
有没有O(n)的排列方法呢？答案是肯定的。注意float('-inf')与float('inf')的使用。

    class Solution(object):
        def maximumProduct(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            l1=l2=l3=float('-inf')
            s1=s2=float('inf')
            for n in nums:
                if n>l1:
                    l1,l2,l3=n,l1,l2
                elif n>l2:
                    l2,l3=n,l2
                elif n>l3:
                    l3=n
                if n<s1:
                    s1,s2=n,s1
                elif n<s2:
                    s2=n
            return max(l1*l2*l3,l1*s1*s2)
                
                