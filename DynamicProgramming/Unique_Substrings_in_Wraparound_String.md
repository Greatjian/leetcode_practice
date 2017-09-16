# 467. Unique Substrings in Wraparound String

Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s. In particular, your input is the string p and you need to output the number of different non-empty substrings of p in the string s.

Note: p consists of only lowercase English letters and the size of p might be over 10000.

    Example 1:
    Input: "a"
    Output: 1

Explanation: Only the substring "a" of string "a" is in the string s.

    Example 2:
    Input: "cac"
    Output: 2

Explanation: There are two substrings "a", "c" of string "cac" in the string s.

    Example 3:
    Input: "zab"
    Output: 6

Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.

## Method:
dp[i]记录字母i开头数组满足条件子集数，max去除重复部分：

    class Solution(object):
        def findSubstringInWraproundString(self, p):
            """
            :type p: str
            :rtype: int
            """
            dp=[0]*26
            pos=1
            for i in range(len(p)):
                if i>0 and (ord(p[i])-ord(p[i-1])==1 or p[i]=='a' and p[i-1]=='z'):
                    pos+=1
                else:
                    pos=1
                dp[ord(p[i])-ord('a')]=max(dp[ord(p[i])-ord('a')],pos);
            return sum(dp)

list外也可用count中的defaultdict计数：

    class Solution(object):
        def findSubstringInWraproundString(self, p):
            """
            :type p: str
            :rtype: int
            """
            pattern = 'zabcdefghijklmnopqrstuvwxyz'
            cmap = collections.defaultdict(int)
            print cmap
            clen = 0
            for c in range(len(p)):
                if c and p[c-1:c+1] not in pattern:
                    clen = 1
                else:
                    clen += 1
                cmap[p[c]] = max(clen, cmap[p[c]])
            print cmap
            return sum(cmap.values())