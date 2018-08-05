

- 076.Minimum Window Substring

s[i:j] is a substring that contains all elements in t when count==0,
count changes when elements in s[i:j] is larger/smaller than that in t:


    class Solution(object):
        def minWindow(self, s, t):
            """
            :type s: str
            :type t: str
            :rtype: str
            """
            d=collections.Counter(t)
            count=len(d)
            i, j=0, 0
            l=float('inf')
            res=""
            while j<len(s):
                if s[j] in d:
                    d[s[j]]-=1
                    if d[s[j]]==0:
                        count-=1
                j+=1
                while count==0:
                    if s[i] in d:
                        d[s[i]]+=1
                        if d[s[i]]==1:
                            count+=1
                    if j-i<l:
                        l=j-i
                        res=s[i:j]
                    i+=1
            return res
            
- 003.Longest Substring Without Repeating Characters

s[i:j] is is a substring that without repeating characters,
count changes when there are more/less than one elements in substring s[i:j]:

    class Solution(object):
        def lengthOfLongestSubstring(self, s):
            """
            :type s: str
            :rtype: int
            """
            d=collections.defaultdict(int)
            count, res=0, 0
            i, j=0, 0
            while j<len(s):
                d[s[j]]+=1
                if d[s[j]]>1:
                    count+=1
                j+=1
                while count>0:
                    d[s[i]]-=1
                    if d[s[i]]==1:
                        count-=1
                    i+=1
                res=max(res, j-i)
            return res
            
- 159.Longest Substring with At Most Two Distinct Characters

count is the number of distinct characters in substring s[i:j] 
(although here can be replaced by len(d)).

count changes when new character is adding or removing from the substring:

    class Solution(object):
        def lengthOfLongestSubstringTwoDistinct(self, s):
            """
            :type s: str
            :rtype: int
            """
            d=collections.defaultdict(int)
            count=0
            res=0
            i, j=0, 0
            while j<len(s):
                d[s[j]]+=1
                if d[s[j]]==1:
                    count+=1
                j+=1
                while count>2:
                    d[s[i]]-=1
                    if d[s[i]]==0:
                        count-=1
                    i+=1
                res=max(res, j-i)
            return res
            
- 438.Find All Anagrams in a String

build the counter from target string (t) and delete by evaluating the current string (s).

s[i:j] contains all exact numbers of characters in target string when count==0,
therefore it's an anagram when they are at the same length.

count changes when the number is less/more than 0.

    class Solution(object):
        def findAnagrams(self, s, p):
            """
            :type s: str
            :type p: str
            :rtype: List[int]
            """
            d=collections.Counter(p)
            count=len(d)
            res=[]
            i, j=0, 0
            while j<len(s):
                if s[j] in d:
                    d[s[j]]-=1
                    if d[s[j]]==0:
                        count-=1
                j+=1
                while count==0:
                    if s[i] in d:
                        d[s[i]]+=1
                        if d[s[i]]==1:
                            count+=1
                    if j-i==len(p):
                        res.append(i)
                    i+=1
            return res
            
- 030.Substring with Concatenation of All Words

    - need to evaluate each starting position i from index 0 to wl-1,
    - for each evaluation, reset count and cur. use cur to compare when target counter (d)
    - we start to reevaluate when a new word is not in d, by setting `i=j+wl` and reset count and cur
    - we add count when the new word is in the d and `cur[word]<d[word]`, or reduce it when it's larger
    - our requirement is met when count==len(words)

code below:

    class Solution(object):
        def findSubstring(self, s, words):
            """
            :type s: str
            :type words: List[str]
            :rtype: List[int]
            """
            if not words:
                return []
            wl=len(words[0])
            for w in words:
                if len(w)!=wl:
                    return []
            res=[]
            d=collections.Counter(words)
            for _ in range(wl):
                cur=collections.defaultdict(int)
                count=0
                i=_
                for j in range(i, len(s)+1-wl, wl):
                    right=s[j:j+wl]
                    if right in d:
                        cur[right]+=1
                        if cur[right]<=d[right]:
                            count+=1
                        while cur[right]>d[right]:
                            left=s[i:i+wl]
                            cur[left]-=1
                            i+=wl
                            if cur[left]<d[left]:
                                count-=1
                        if count==len(words):
                            res.append(i)
                            left=s[i:i+wl]
                            cur[left]-=1
                            i+=wl
                            count-=1
                    else:
                        cur=collections.defaultdict(int)
                        count = 0
                        i=j+wl
            return res