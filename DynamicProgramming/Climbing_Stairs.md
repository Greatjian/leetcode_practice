# 070. Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

## Method:
递推法：

    class Solution(object):
        def climbStairs(self, n):
            """
            :type n: int
            :rtype: int
            """
            if n==1:
                return 1
            if n==2:
                return 2
            nums=[0 for i in range(n)]
            nums[0],nums[1]=1,2
            for i in range(2,n):
                nums[i]=nums[i-2]+nums[i-1]
            return nums[-1]
            
## Solution:
迭代，减少空间复杂度：

    class Solution(object):
        def climbStairs(self, n):
            """
            :type n: int
            :rtype: int
            """
            if n <= 0:
                return 0
            a = b = 1
            for _ in xrange(n):
                a, b = b, a+b
            return a;