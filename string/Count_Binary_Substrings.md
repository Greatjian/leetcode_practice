# 696. Count Binary Substrings

Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:

    Input: "00110011"
    Output: 6
    Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

    Example 2:
    Input: "10101"
    Output: 4
    Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

Note:

- s.length will be between 1 and 50,000.
- s will only consist of "0" or "1" characters.

## Method:

每次0，1变化时比较：

    class Solution(object):
        def countBinarySubstrings(self, s):
            """
            :type s: str
            :rtype: int
            """
            zc, oc=0, 0
            res=0
            if s[0]=='0':
                zc+=1
            else:
                oc+=1
            for i in range(1, len(s)):
                if s[i]=='0':
                    if s[i-1]=='1':
                        res+=min(zc, oc)
                        zc=1
                    else:
                        zc+=1
                else:
                    if s[i-1]=='0':
                        res+=min(zc, oc)
                        oc=1
                    else:
                        oc+=1
            res+=min(zc, oc)
            return res
            
## Solution:

s.replace():

    class Solution(object):
        def countBinarySubstrings(self, s):
            """
            :type s: str
            :rtype: int
            """
            s = map(len, s.replace('01','0 1').replace('10','1 0').split())
            return sum(min(s[i-1],s[i]) for i in range(1, len(s)))