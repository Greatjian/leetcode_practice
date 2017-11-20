# 166. Fraction to Recurring Decimal

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

- Given numerator = 1, denominator = 2, return "0.5".
- Given numerator = 2, denominator = 1, return "2".
- Given numerator = 2, denominator = 3, return "0.(6)".

## Method:

    class Solution(object):
        def fractionToDecimal(self, numerator, denominator):
            """
            :type numerator: int
            :type denominator: int
            :rtype: str
            """
            if numerator%denominator==0:
                return str(numerator//denominator)
            res = []
            res+=['-'] if numerator//denominator<0 else ['']
            numerator=abs(numerator)
            denominator=abs(denominator)
            res+=[str(numerator//denominator)+'.']
            numerator%=denominator
            d={}
            i=len(res)
            while numerator not in d:
                d[numerator]=i
                res+=[str((numerator * 10) // denominator)]
                numerator=(numerator * 10) % denominator
                i+=1
                if numerator==0:
                    return ''.join(res)
            res.insert(d[numerator], '(')
            return ''.join(res+[')'])
            
简写：

    class Solution(object):
        def fractionToDecimal(self, numerator, denominator):
            """
            :type numerator: int
            :type denominator: int
            :rtype: str
            """
            res=['-'] if numerator//denominator<0 else ['']
            numerator, denominator=abs(numerator), abs(denominator)
            res+=[str(numerator//denominator)]
            if numerator%denominator:
                res+=['.']
            numerator%=denominator
            d={}
            i=len(res)
            while numerator and numerator not in d:
                d[numerator]=i
                res+=[str((numerator * 10) // denominator)]
                numerator=(numerator * 10) % denominator
                i+=1
            if numerator:
                res.insert(d[numerator], '(')
                res.append(')')
            return ''.join(res)