# 161. One Edit Distance

Given two strings S and T, determine if they are both one edit distance apart.

## Method:

O(n^2), tle:

    class Solution(object):
        def isOneEditDistance(self, s, t):
            """
            :type s: str
            :type t: str
            :rtype: bool
            """
            ls, lt=len(s), len(t)
            if abs(ls-lt)>1 or s==t:
                return False
            d=set()
            for i in range(ls):
                d.add(s[:i]+'*'+s[i+1:])
                d.add(s[:i]+'*'+s[i:])
            d.add(s+'*')
            for i in range(lt):
                if (t[:i]+'*'+t[i+1:]) in d or (t[:i]+'*'+t[i:]) in d:
                    return True
            return (t+'*') in d
            
## Solution:

三种情况，逐位比较：

    class Solution(object):
        def isOneEditDistance(self, s, t):
            """
            :type s: str
            :type t: str
            :rtype: bool
            """
            for i in range(min(len(s), len(t))):
                if s[i]!=t[i]:
                    if len(s)==len(t):
                        return s[i+1:]==t[i+1:]
                    elif len(t)>len(s):
                        return t[i+1:]==s[i:]
                    else:
                        return s[i+1:]==t[i:]               
            return abs(len(s)-len(t))==1
            
中间判断部分可以简写：

    for i in range(min(len(s), len(t))):
        if s[i] != t[i]:
            return s[i + (1 if len(s) >= len(t) else 0):] == t[i + (1 if len(s) <= len(t) else 0):]
    return abs(len(s) - len(t)) == 1