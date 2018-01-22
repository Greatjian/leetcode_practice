# 137. Single Number II

Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:
- Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

## Solution:

bit manipulation:

    class Solution(object):
        def singleNumber(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            # we need to implement a three-time counter(base 3) that if a bit appears three time ,it will be zero.
            # curent  income  ouput
            # ab      c/c     ab/ab
            # 00      1/0     01/00
            # 01      1/0     10/01
            # 10      1/0     00/10
            # a=~abc+a~b~c;
            # b=~a~bc+~ab~c;
            a=0;
            b=0;
            for c in nums:
                ta=(~a&b&c)|(a&~b&~c)
                b=(~a&~b&c)|(~a&b&~c)
                a=ta
            # we need find the number that is 01,10 => 1, 00 => 0.
            return a|b
            
sum求和：

    class Solution(object):
        def singleNumber(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            return (3*sum(set(nums)) - sum(nums))/2