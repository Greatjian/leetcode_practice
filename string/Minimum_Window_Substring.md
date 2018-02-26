# 076. Minimum Window Substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

    For example,
    S = "ADOBECODEBANC"
    T = "ABC"
    Minimum window is "BANC".

Note:
- If there is no such window in S that covers all characters in T, return the empty string "".

- If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

## Method:

two sliding window pointers, two iterate pointers:

    class Solution(object):
        def minWindow(self, s, t):
            """
            :type s: str
            :type t: str
            :rtype: str
            """
            d=collections.Counter(t)
            counter=len(t)
            begin, end=0, 0
            minStart, gap=0, len(s)+1
            while end<len(s):
                if s[end] in d:
                    if d[s[end]]>0:
                        counter-=1
                    d[s[end]]-=1
                while counter==0:
                    if end-begin+1<gap:
                        gap=end-begin+1
                        minStart=begin
                    if s[begin] in d:
                        d[s[begin]]+=1
                        if d[s[begin]]>0:
                            counter+=1
                    begin+=1
                end+=1
            return s[minStart:minStart+gap] if gap!=len(s)+1 else ""