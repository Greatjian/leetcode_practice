# 058. Length of Last Word

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 

    Given s = "Hello World",
    return 5.

## Method:
s.split(' ')

    class Solution(object):
        def lengthOfLastWord(self, s):
            """
            :type s: str
            :rtype: int
            """
            a=s.split(' ')
            for b in a[::-1]:
                if len(b):
                    return len(b)
            return 0
            
s.split()
            
    class Solution(object):
        def lengthOfLastWord(self, s):
            """
            :type s: str
            :rtype: int
            """
            a=s.split()
            return len(a[-1]) if a else 0