# 415. Add Strings

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

- The length of both num1 and num2 is < 5100.
- Both num1 and num2 contains only digits 0-9.
- Both num1 and num2 does not contain any leading zero.
- You must not use any built-in BigInteger library or convert the inputs to integer directly.

## Method:

using built-in library (int):

    class Solution(object):
        def addStrings(self, num1, num2):
            """
            :type num1: str
            :type num2: str
            :rtype: str
            """
            return str(int(num1)+int(num2))
            
using carryon by digit:

    class Solution(object):
        def addStrings(self, num1, num2):
            """
            :type num1: str
            :type num2: str
            :rtype: str
            """
            if len(num1)>len(num2):
                num2='0'*(len(num1)-len(num2))+num2
            else:
                num1='0'*(len(num2)-len(num1))+num1
            carryon=0
            res=[]
            for i in range(len(num1)-1, -1, -1):
                carryon+=ord(num1[i])+ord(num2[i])-2*ord('0')
                res.append(str(carryon%10))
                carryon/=10
            if carryon:
                res.append(str(carryon))
            return ''.join(res[::-1])
                
                