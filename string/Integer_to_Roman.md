# 12. Integer to Roman

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

## Method:

复杂版：

    class Solution(object):
        def intToRoman(self, num):
            """
            :type num: int
            :rtype: str
            """
            res=''
            while num>=1000:
                res+='M'
                num-=1000
            if num>=900:
                res+="CM"
                num-=900
            while num>=500:
                res+='D'
                num-=500
            if num>=400:
                res+='CD'
                num-=400
            while num>=100:
                res+='C'
                num-=100
            if num>=90:
                res+='XC'
                num-=90
            while num>=50:
                res+='L'
                num-=50
            if num>=40:
                res+='XL'
                num-=40
            while num>=10:
                res+='X'
                num-=10
            if num>=9:
                res+='IX'
                num-=9
            while num>=5:
                res+='V'
                num-=5
            if num>=4:
                res+='IV'
                num-=4
            while num>=1:
                res+='I'
                num-=1
            return res
            
整理后简写：

    class Solution(object):
        def intToRoman(self, num):
            """
            :type num: int
            :rtype: str
            """
            res=''
            nums=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
            ans=['M', "CM", 'D', "CD", 'C', "XC", 'L', "XL", 'X', "IX", 'V', "IV", 'I']
            for i, v in enumerate(nums):
                while num>=v:
                    res+=ans[i]
                    num-=v
            return res
            
## Solution:

    class Solution(object):
        def intToRoman(self, num):
            """
            :type num: int
            :rtype: str
            """
            thou=['', 'M', 'MM', 'MMM']
            hun=['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
            ten=['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
            one=['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
            return thou[num/1000]+hun[(num%1000)/100]+ten[(num%100)/10]+one[num%10]