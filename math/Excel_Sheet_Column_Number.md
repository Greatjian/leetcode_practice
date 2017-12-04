# 171. Excel Sheet Column Number

Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    
## Method:

string slicing is slow:

    class Solution(object):
        def titleToNumber(self, s):
            """
            :type s: str
            :rtype: int
            """
            res=0
            while s:
                res=res*26+ord(s[0])-ord('A')+1
                s=s[1:]
            return res
            
one for-loop:

    class Solution(object):
        def titleToNumber(self, s):
            """
            :type s: str
            :rtype: int
            """
            res=0
            for i in s:
                res=res*26+ord(i)-ord('A')+1
            return res
            
## Solution:

solve recursively:

    class Solution(object):
        def titleToNumber(self, s):
            """
            :type s: str
            :rtype: int
            """
            if not s:
                return 0
            return ord(s[-1])-ord('A')+1+26*self.titleToNumber(s[:-1])