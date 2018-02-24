# 091. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

## Solution:

    class Solution(object):
        def numDecodings(self, s):
            """
            :type s: str
            :rtype: int
            """
            if s == "" or s[0] == '0':
                return 0
            dp=[1,1]
            for i in range(2,len(s) + 1):
                if 10 <= int(s[i - 2 : i]) <=26 and s[i - 1] != '0':
                    dp.append(dp[i - 1] + dp[i - 2])
                elif int(s[i-2 : i]) == 10 or int(s[i - 2 : i]) == 20:
                    dp.append(dp[i - 2])
                elif s[i-1] != '0':
                    dp.append(dp[i-1])
                else:
                    return 0
    
            return dp[len(s)]

二刷:

    class Solution(object):
        def numDecodings(self, s):
            """
            :type s: str
            :rtype: int
            """
            dp=[1]*(len(s)+1)
            for i in range(len(s)-1, -1, -1):
                if s[i]=='0':
                    dp[i]=0
                elif i!=len(s)-1 and int(s[i:i+2])<=26:
                    dp[i]=dp[i+1]+dp[i+2]
                else:
                    dp[i]=dp[i+1]
            return dp[0] if s else 0
         
            
    class Solution(object):
        def numDecodings(self, s):
            """
            :type s: str
            :rtype: int
            """
            e0, e1, e2=1, 0, 0
            for i in s:
                a, b, c=e0, e1, e2
                e0=(i>'0')*a+b+(i<='6')*c
                e1=(i=='1')*a
                e2=(i=='2')*a
            return e0 if s else 0