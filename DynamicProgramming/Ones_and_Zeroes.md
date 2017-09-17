# 474. Ones and Zeroes

In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

Note:

- The given numbers of 0s and 1s will both not exceed 100
- The size of given string array won't exceed 600.

Example 1:

    Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
    Output: 4
    
    Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”

Example 2:

    Input: Array = {"10", "0", "1"}, m = 1, n = 1
    Output: 2
    
    Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".

## Method:

二维01背包问题（Knapsack Problem）:

一个很好的[intro](http://love-oriented.com/pack/)

    class Solution(object):
        def findMaxForm(self, strs, m, n):
            """
            :type strs: List[str]
            :type m: int
            :type n: int
            :rtype: int
            """
            dp = [[0] * (n + 1) for x in range(m + 1)]
            for s in strs:
                zero, one = s.count('0'), s.count('1')
                for x in range(m, zero - 1, -1):
                    for y in range(n, one - 1, -1):
                        dp[x][y] = max(dp[x - zero][y - one] + 1, dp[x][y])
            return dp[-1][-1]