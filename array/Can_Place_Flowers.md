# 605. Can Place Flowers

Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:

    Input: flowerbed = [1,0,0,0,1], n = 1
    Output: True

Example 2:

    Input: flowerbed = [1,0,0,0,1], n = 2
    Output: False

Note:
- The input array won't violate no-adjacent-flowers rule.
- The input array size is in the range of [1, 20000].
- n is a non-negative integer which won't exceed the input array size.

## Method:
尝试将数组转换为字符串并分割，需根据首尾即字符串长度情况分类讨论：

    class Solution(object):
        def canPlaceFlowers(self, flowerbed, n):
            """
            :type flowerbed: List[int]
            :type n: int
            :rtype: bool
            """
            count=0
            f1=[str(i) for i in flowerbed]
            f2=''.join(f1)
            f3=f2.split('1')
            if len(f3)>1:
                for i in range(len(f3)):
                    if i==0 or i==len(f3)-1:
                        count+=(len(f3[i]))//2
                    else:
                        if len(f3[i]):
                            count+=(len(f3[i])-1)//2
            else:
                count+=(len(f3[0])+1)//2
            return count>=n        

## Solution:
贪心算法（Greedy Algorithm）:
从左向右遍历flowerbed，将满足要求的0设为1。计数与n比较即可。

    class Solution(object):
        def canPlaceFlowers(self, flowerbed, n):
            """
            :type flowerbed: List[int]
            :type n: int
            :rtype: bool
            """
            ans = 0
            for i, v in enumerate(flowerbed):
                if v: continue
                if i > 0 and flowerbed[i - 1]: continue
                if i < len(flowerbed) - 1 and flowerbed[i + 1]: continue
                ans += 1
                flowerbed[i] = 1
            return ans >= n
            
另一种方式：

    class Solution(object):
        def canPlaceFlowers(self, flowerbed, n):
            """
            :type flowerbed: List[int]
            :type n: int
            :rtype: bool
            """
            for idx in range(len(flowerbed)):
                if flowerbed[idx]==0 and (idx==0 or flowerbed[idx-1]==0) and (idx==len(flowerbed)-1 or flowerbed[idx+1]==0):
                    flowerbed[idx]=1
                    n-=1
            return n<=0