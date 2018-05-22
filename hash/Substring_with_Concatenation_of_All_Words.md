# 030. Substring with Concatenation of All Words

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

    Input:
      s = "barfoothefoobarman",
      words = ["foo","bar"]
    Output: [0,9]
    Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
    The output order does not matter, returning [9,0] is fine too.

Example 2:

    Input:
      s = "wordgoodstudentgoodword",
      words = ["word","student"]
    Output: []
    
## Method:

check each left index, O(nl), where l=len(words)*words[0], tle (173/174):

    class Solution(object):
        def findSubstring(self, s, words):
            """
            :type s: str
            :type words: List[str]
            :rtype: List[int]
            """
            if not words:
                return []
            l=len(words[0])
            for w in words:
                if len(w)!=l:
                    return []
                    
            res=[]
            for j in range(len(s)-l*len(words)+1):
                i=j
                flag=True
                S=collections.Counter(words)
                while i<j+l*len(words):
                    if s[i:i+l] in S and S[s[i:i+l]]>0:
                        S[s[i:i+l]]-=1
                        i+=l
                    else:
                        flag=False
                        break
                if flag:
                    res.append(j)
            return res
            
## Solution:

sliding window, O(n):

    class Solution(object):
        def findSubstring(self, s, words):
            """
            :type s: str
            :type words: List[str]
            :rtype: List[int]
            """
            if not words:
                return []
            l=len(words[0])
            for w in words:
                if len(w)!=l:
                    return []
            res=[]
            for i in range(l):
                c=collections.Counter(words)
                left, right=i, i
                while right+l<len(s)+1 and left<len(s)-l*len(words)+1:
                    if s[right:right+l] in c and c[s[right:right+l]]>0:
                        c[s[right:right+l]]-=1
                        right+=l
                    elif s[right:right+l] not in c:
                        left=right+l
                        right=left
                        c=collections.Counter(words)
                    elif s[right:right+l] in c and c[s[right:right+l]]==0:
                        while left<right and s[left:left+l]!=s[right:right+l]:
                            c[s[left:left+l]]+=1
                            left+=l
                        left+=l
                        right+=l
                    if right-left==l*len(words):
                        res.append(left)
            return res