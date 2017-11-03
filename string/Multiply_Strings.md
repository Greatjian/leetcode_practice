# 043. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

- The length of both num1 and num2 is < 110.
- Both num1 and num2 contains only digits 0-9.
- Both num1 and num2 does not contain any leading zero.
- You must not use any built-in BigInteger library or convert the inputs to integer directly.

    
    return str(int(num1)*int(num2))
    
## Method:

    class Solution(object):
        def multiply(self, num1, num2):
            """
            :type num1: str
            :type num2: str
            :rtype: str
            """
            num1=map(int, num1[::-1])
            num2=map(int, num2[::-1])
            ans=[0]*(len(num1)+len(num2))
            
            for i in range(len(num1)):
                for j in range(len(num2)):
                    ans[i+j]+=num1[i]*num2[j]
            
            carry=0
            for i in range(len(ans)):
                ans[i]+=carry
                carry=ans[i]/10
                ans[i]%=10
            
            for k in range(len(ans)-1,-1,-1):
                if ans[k]!=0:
                    break
            
            ans=map(str, ans[:k+1])
            return ''.join(ans[::-1])