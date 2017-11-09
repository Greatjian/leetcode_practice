# 434. Number of Segments in a String

Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

    Input: "Hello, my name is John"
    Output: 5
    
## Method:

s.split():

    class Solution(object):
        def countSegments(self, s):
            """
            :type s: str
            :rtype: int
            """
            return len(s.split())
            
## Solution:

iteration:

    class Solution(object):
        def countSegments(self, s):
            """
            :type s: str
            :rtype: int
            """
            res=0
            for i in range(len(s)):
                if s[i]!=' ' and (i==0 or s[i-1]==' '):
                    res+=1
            return res