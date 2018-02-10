# 312. Burst Balloons

Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note: 

(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.

(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

    Example:
    
    Given [3, 1, 5, 8]
    
    Return 167
    
        nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
       coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
       
## Method:

reversed thinking, bottom up dp or top down divide and conquer with memorization:

    class Solution(object):
        def maxCoins(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            n=[1 for _ in range(len(nums)+2)]
            n[1:-1]=nums
            dp=[[0]*len(n) for _ in range(len(n))]
            
            for k in range(2, len(n)):
                for left in range(len(n)-k):
                    right=left+k
                    for i in range(left+1, right):
                        dp[left][right] = max(dp[left][right], n[left]*n[i]*n[right]+dp[left][i]+dp[i][right])
            return dp[0][-1]
                    
                    
    class Solution(object):
        def maxCoins(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            n=[1 for _ in range(len(nums)+2)]
            n[1:-1]=nums
            d={}
            
            def helper(lo, hi):
                if lo>hi:
                    return 0
                if (lo, hi) in d:
                    return d[lo, hi]
                coin=0
                for i in range(lo, hi+1):
                    coin=max(coin, helper(lo, i-1)+n[lo-1]*n[i]*n[hi+1]+helper(i+1, hi))
                d[(lo, hi)]=coin
                return coin
            
            return helper(1, len(n)-2)
                    