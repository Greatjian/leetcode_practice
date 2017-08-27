# 264. Ugly Number II

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number, and n does not exceed 1690.

## Method:

找规律，ugly number后面出现的数为列表前出现数字的2，3，5倍，按顺序加入即可：

    class Solution(object):
        def nthUglyNumber(self, n):
            """
            :type n: int
            :rtype: int
            """
            res=[1]
            i2=i3=i5=0
            while len(res)<n:
                new=min(res[i2]*2,res[i3]*3,res[i5]*5)
                res.append(new)
                if new==res[i2]*2:
                    i2+=1
                if new==res[i3]*3:
                    i3+=1
                if new==res[i5]*5:
                    i5+=1
            return res[-1]
                