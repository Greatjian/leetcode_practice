# 13. Roman to Integer

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

## Method:

    class Solution(object):
        def romanToInt(self, s):
            """
            :type s: str
            :rtype: int
            """
            res=0
            if "IV" in s or "IX" in s:
                res-=2
            if "XL" in s or "XC" in s:
                res-=20
            if "CD" in s or "CM" in s:
                res-=200
            d={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
            for i in s:
                res+=d[i]
            return res
            
## Solution:

    class Solution(object):
        def romanToInt(self, s):
            """
            :type s: str
            :rtype: int
            """
            res=0
            d={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
            for i in range(len(s)-1):
                if d[s[i]]>=d[s[i+1]]:
                    res+=d[s[i]]
                else:
                    res-=d[s[i]]
            return res+d[s[-1]]