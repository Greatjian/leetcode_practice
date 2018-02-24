# 639. Decode Ways II

A message containing letters from A-Z is being encoded to numbers using the following mapping way:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the numbers from 1 to 9.

Given the encoded message containing digits and the character '*', return the total number of ways to decode it.

Also, since the answer may be very large, you should return the output mod 109 + 7.

    Example 1:
    Input: "*"
    Output: 9
    Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".
    
    Example 2:
    Input: "1*"
    Output: 9 + 9 = 18

Note:
- The length of the input string will fit in range [1, 105].
- The input string will only contain the character '*' and digits '0' - '9'.

## Method:

    class Solution(object):
        def numDecodings(self, s):
            """
            :type s: str
            :rtype: int
            """
            MOD=10**9+7
            e0, e1, e2=1, 0, 0
            for i in s:
                a, b, c=e0, e1, e2
                if i=='*':
                    e0=9*a+9*b+6*c
                    e1=a
                    e2=a
                else:
                    e0=(i>'0')*a+b+(i<='6')*c
                    e1=(i=='1')*a
                    e2=(i=='2')*a
                e0%=MOD
                e1%=MOD
                e2%=MOD
            return e0
            