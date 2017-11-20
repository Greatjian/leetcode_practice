# 205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,

    Given "egg", "add", return true.
    
    Given "foo", "bar", return false.
    
    Given "paper", "title", return true.

Note:
- You may assume both s and t have the same length.

## Method:

    class Solution(object):
        def isIsomorphic(self, s, t):
            """
            :type s: str
            :type t: str
            :rtype: bool
            """
            d1, d2=collections.defaultdict(int), collections.defaultdict(int)
            for i in range(len(s)):
                if (s[i] in d1) ^ (t[i] in d2):
                    return False
                if d1[s[i]]!=d2[t[i]]:
                    return False
                d1[s[i]]=d2[t[i]]=i
            return True
            
## Solution;

len(set):

    class Solution(object):
        def isIsomorphic(self, s, t):
            """
            :type s: str
            :type t: str
            :rtype: bool
            """
            return len(set(zip(s, t))) == len(set(s)) == len(set(t))