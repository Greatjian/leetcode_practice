# 326. Power of Three

Given an integer, write a function to determine if it is a power of three.

Follow up:
- Could you do it without using any loop / recursion?

## Method:

recursion:

    class Solution(object):
        def isPowerOfThree(self, n):
            """
            :type n: int
            :rtype: bool
            """
            if n==1:
                return True
            if n % 3 or n<=0:
                return False
            return self.isPowerOfThree(n/3)
            
iteration:

    class Solution(object):
        def isPowerOfThree(self, n):
            """
            :type n: int
            :rtype: bool
            """
            while n>0:
                if n==1:
                    return True
                if n % 3:
                    return False
                n/=3
            return False
            
## Solution:

3**20 is bigger than int:

    class Solution(object):
        def isPowerOfThree(self, n):
            """
            :type n: int
            :rtype: bool
            """
            // int(math.log(2**31, 3))=19
            return n>0 and 3**19 % n==0