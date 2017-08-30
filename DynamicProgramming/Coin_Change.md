# 322. Coin Change

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

    Example 1:
    coins = [1, 2, 5], amount = 11
    return 3 (11 = 5 + 5 + 1)
    
    Example 2:
    coins = [2], amount = 3
    return -1.

Note:
You may assume that you have an infinite number of each kind of coin.

## Method:
贪心法：局部最优不能达到全局最优，不行：

    class Solution(object):
        def coinChange(self, coins, amount):
            """
            :type coins: List[int]
            :type amount: int
            :rtype: int
            """
            if amount==0:
                return 0
            coins.sort()
            count=0
            for i in range(len(coins)-1,-1,-1):
                if coins[i]<=amount:
                    r=amount-coins[i]
                    count+=1
                    while r>=coins[i]:
                        r-=coins[i]
                        count+=1
                    if r==0:
                        return count
                    amount=r
                if i==0 and coins[i]>amount:
                    return -1
            
## Solution:

动态规划：

状态转移方程：dp[x + c] = min(dp[x] + 1, dp[x + c])

    class Solution(object):
        def coinChange(self, coins, amount):
            """
            :type coins: List[int]
            :type amount: int
            :rtype: int
            """
            dp=[0]+[-1]*amount
            for i in range(amount):
                for r in coins:
                    if i+r<=amount and dp[i]>=0:
                        if dp[i+r]<0 or dp[i+r]>dp[i]+1:
                            dp[i+r]=dp[i]+1
            return dp[-1]