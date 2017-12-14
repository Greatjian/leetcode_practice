# 367. Valid Perfect Square

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

    Input: 16
    Returns: True

Example 2:

    Input: 14
    Returns: False

## Method:

tle:

    class Solution(object):
        def isPerfectSquare(self, num):
            """
            :type num: int
            :rtype: bool
            """
            i=0
            while i*i<=num:
                if i*i==num:
                    return True
            return False
            
1+3+5+...:

    class Solution(object):
        def isPerfectSquare(self, num):
            """
            :type num: int
            :rtype: bool
            """
            i=1
            while num>=0:
                if num==0:
                    return True
                num-=i
                i+=2
            return False
            
## Solution:

binary search:

    class Solution(object):
        def isPerfectSquare(self, num):
            """
            :type num: int
            :rtype: bool
            """
            lo, hi=0, num
            while lo<=hi:
                mid=(lo+hi)/2
                if mid**2==num:
                    return True
                if mid**2<num:
                    lo=mid+1
                else:
                    hi=mid-1
            return False
            
iterative method, similar to [sqrt](/math/Sqrt(x).md)

    lass Solution(object):
        def isPerfectSquare(self, num):
            """
            :type num: int
            :rtype: bool
            """
            res = num
            while res * res > num:
                res = (res + num/res)/2
            return res*res == num