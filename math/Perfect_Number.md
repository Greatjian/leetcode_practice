# 507. Perfect Number

We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.

Example:

    Input: 28
    Output: True
    Explanation: 28 = 1 + 2 + 4 + 7 + 14

Note: The input number n will not exceed 100,000,000. (1e8)

## Method:

tle:

    class Solution(object):
        def checkPerfectNumber(self, num):
            """
            :type num: int
            :rtype: bool
            """
            res=0
            for i in range(1, num/2+1):
                if num%i==0:
                    res+=i
            return res==num
            
## Solution:

减少比较次数，num/2到num**0.5:

    class Solution(object):
        def checkPerfectNumber(self, num):
            """
            :type num: int
            :rtype: bool
            """
            if num<=1:
                return False
            res=1
            for i in range(2, int(num**0.5)+1):
                if num%i==0:
                    res+=i+num/i
            return res==num
            
            
