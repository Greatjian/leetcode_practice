# 007. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

    Input: 123
    Output:  321

Example 2:

    Input: -123
    Output: -321

Example 3:

    Input: 120
    Output: 21

Note:
- Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. 
- For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

## Method:

    class Solution(object):
        def reverse(self, x):
            """
            :type x: int
            :rtype: int
            """
            res=0
            y=abs(x)
            while y:
                res+=y%10
                y/=10
                res*=10
            if res/10>2**31:
                return 0
            else:
                return res/10 if x>0 else -1*res/10
                
            