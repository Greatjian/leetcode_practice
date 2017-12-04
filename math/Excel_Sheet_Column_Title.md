# 168. Excel Sheet Column Title

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    
## Method:

    class Solution(object):
        def convertToTitle(self, n):
            """
            :type n: int
            :rtype: str
            """
            res=''
            while n:
                res+=chr((n-1)%26+ord('A'))
                n=(n-1)/26
            return res[::-1]