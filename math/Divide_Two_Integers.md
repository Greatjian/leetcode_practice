# 029. Divide Two Integers

Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.

## Method:

tle:

    class Solution(object):
        def divide(self, dividend, divisor):
            """
            :type dividend: int
            :type divisor: int
            :rtype: int
            """
            if dividend>2**31:
                return 6184773855
            if dividend<-2**31:
                return -6184773855
            count=0
            sign=1
            if dividend * divisor<0:
                sign=-1
            dividend, divisor=abs(dividend), abs(divisor)
            while dividend>=divisor:
                dividend-=divisor
                count+=1
            return sign * count
            
## Solution:

不断增加divisor:

    class Solution(object):
        def divide(self, dividend, divisor):
            """
            :type dividend: int
            :type divisor: int
            :rtype: int
            """
            positive = (dividend < 0) == (divisor < 0)
            dividend, divisor = abs(dividend), abs(divisor)
            res = 0
            while dividend >= divisor:
                temp, i = divisor, 1
                while dividend >= temp:
                    dividend -= temp
                    res += i
                    i *= 2
                    temp *= 2
            if not positive:
                res = -res
            return min(max(-2**31-1, res), 2**31-1)