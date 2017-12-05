# 258. Add Digits

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

    Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
- Could you do it without any loop/recursion in O(1) runtime?

## Method:

recursion:

    class Solution(object):
        def addDigits(self, num):
            """
            :type num: int
            :rtype: int
            """
            if num<10:
                return num
            return self.addDigits(num%10+self.addDigits(num/10))
            
or:

    class Solution(object):
        def addDigits(self, num):
            """
            :type num: int
            :rtype: int
            """
            if num<10:
                return num
            return self.addDigits(num%10+num/10)
            
iteration:

    class Solution(object):
        def addDigits(self, num):
            """
            :type num: int
            :rtype: int
            """
            while num>=10:
                tmp=0
                while num:
                    tmp+=num%10
                    num/=10
                num=tmp
            return num
            
## Solution:

    class Solution(object):
        def addDigits(self, num):
            """
            :type num: int
            :rtype: int
            """
            if not num:
                return 0
            return (num-1)%9+1