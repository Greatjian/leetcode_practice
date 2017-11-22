# 438. Find All Anagrams in a String

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:
    
    Input:
    s: "cbaebabacd" p: "abc"
    
    Output:
    [0, 6]
    
    Explanation:
    The substring with start index = 0 is "cba", which is an anagram of "abc".
    The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
    
    Input:
    s: "abab" p: "ab"
    
    Output:
    [0, 1, 2]
    
    Explanation:
    The substring with start index = 0 is "ab", which is an anagram of "ab".
    The substring with start index = 1 is "ba", which is an anagram of "ab".
    The substring with start index = 2 is "ab", which is an anagram of "ab".
    
## Method:

O(n2) tle:

    class Solution(object):
        def findAnagrams(self, s, p):
            """
            :type s: str
            :type p: str
            :rtype: List[int]
            """
            d=collections.Counter(p)
            res=[]
            for i in range(len(s)-len(p)+1):
                if collections.Counter(s[i:i+len(p)])==d:
                    res.append(i)
            return res
            
O(n)后加前减:

    class Solution(object):
        def findAnagrams(self, s, p):
            """
            :type s: str
            :type p: str
            :rtype: List[int]
            """
            d1=collections.Counter(p)
            d2=collections.defaultdict(int)
            res=[]
            for i in range(len(s)):
                d2[s[i]]+=1
                if i>=len(p):
                    d2[s[i-len(p)]]-=1
                if set(j for j in d2.items() if j[1]!=0)==set(d1.items()):
                    res.append(i-len(p)+1)
            return res
            
dict判断相等更快：

    class Solution(object):
        def findAnagrams(self, s, p):
            """
            :type s: str
            :type p: str
            :rtype: List[int]
            """
            d1=collections.Counter(p)
            d2=collections.defaultdict(int)
            res=[]
            for i in range(len(s)):
                d2[s[i]]+=1
                if i>=len(p):
                    if d2[s[i-len(p)]]==1:
                        del d2[s[i-len(p)]]
                    else:
                        d2[s[i-len(p)]]-=1
                if d2==d1:
                    res.append(i-len(p)+1)
            return res
            
使用list记录：

    class Solution(object):
        def findAnagrams(self, s, p):
            """
            :type s: str
            :type p: str
            :rtype: List[int]
            """
            d1, d2=[0]*26, [0]*26
            for k in p:
                d1[ord(k)-ord('a')]+=1
            res=[]
            for i in range(len(s)):
                d2[ord(s[i])-ord('a')]+=1
                if i>=len(p):
                    d2[ord(s[i-len(p)])-ord('a')]-=1
                if d2==d1:
                    res.append(i-len(p)+1)
            return res