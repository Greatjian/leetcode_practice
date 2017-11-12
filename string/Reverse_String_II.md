# 541. Reverse String II

Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.

Example:

    Input: s = "abcdefg", k = 2
    Output: "bacdfeg"

Restrictions:
- The string consists of lower English letters only.
- Length of the given string and k will in the range [1, 10000]

## Method:

recursion:

    class Solution(object):
        def reverseStr(self, s, k):
            """
            :type s: str
            :type k: int
            :rtype: str
            """
            if not s:
                return ''
            return s[:k][::-1]+s[k:2*k]+self.reverseStr(s[2*k:], k)
            
## Solution:

    class Solution(object):
        def reverseStr(self, s, k):
            """
            :type s: str
            :type k: int
            :rtype: str
            """
            s=list(s)
            for i in range(0, len(s), 2*k):
                s[i:i+k]=s[i:i+k][::-1]
            return ''.join(s)