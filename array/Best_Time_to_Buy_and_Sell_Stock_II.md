# 122. Best Time to Buy and Sell Stock II

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

## Method:
总收益分解为若干大减小值的和：

    class Solution(object):
        def maxProfit(self, prices):
            """
            :type prices: List[int]
            :rtype: int
            """
            profit=0
            if prices:
                loprice=hiprice=prices[0]
                for i in range(1,len(prices)):
                    if prices[i]>prices[i-1]:
                        hiprice=prices[i]
                        profit+=hiprice-loprice
                        loprice=prices[i]
                    else:
                        loprice=prices[i]
            return profit
## Solution:

    class Solution(object):
        def maxProfit(self, prices):
            """
            :type prices: List[int]
            :rtype: int
            """
            ans = 0
            if prices:
                lo = prices[0]
                for price in prices:
                    if price>lo:
                        ans += price-lo
                    lo = price
            return ans