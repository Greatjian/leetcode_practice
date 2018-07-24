# 340. Longest Substring with At Most K Distinct Characters

Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,

T is "ece" which its length is 3.

## Method:

sliding window using dict:

    class Solution(object):
        def lengthOfLongestSubstringKDistinct(self, s, k):
            """
            :type s: str
            :type k: int
            :rtype: int
            """
            d=collections.defaultdict(int)
            i=0
            res=0
            for j in range(len(s)):
                d[s[j]]+=1
                while len(d)>k:
                    d[s[i]]-=1
                    if d[s[i]]==0:
                        del d[s[i]]
                    i+=1
                res=max(res, j-i+1)
            return res
            
del takes O(k), total is O(nk). To optimize without using del, we add cnt and update
in the process, this will make O(n) overall:

    class Solution(object):
        def lengthOfLongestSubstringKDistinct(self, s, k):
            """
            :type s: str
            :type k: int
            :rtype: int
            """
            d=collections.defaultdict(int)
            i, cnt=0, 0
            res=0
            for j in range(len(s)):
                if d[s[j]]==0:
                    cnt+=1
                d[s[j]]+=1
                while cnt>k:
                    d[s[i]]-=1
                    if d[s[i]]==0:
                        cnt-=1
                    i+=1
                res=max(res, j-i+1)
            return res

## Solution:

use dict to memorize last occurence for each character.

it's O(nk) using del, but in Java, treemap will make it O(nlogk):

    class Solution(object):
        def lengthOfLongestSubstringKDistinct(self, s, k):
            """
            :type s: str
            :type k: int
            :rtype: int
            """
            d={}
            i=0
            res=0
            for j in range(len(s)):
                d[s[j]]=j
                if len(d)>k:
                    val=min(d.values())
                    del d[s[val]]
                    i=val+1
                res=max(res, j-i+1)
            return res