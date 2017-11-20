# 290. Word Pattern

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

    Examples:
    pattern = "abba", str = "dog cat cat dog" should return true.
    pattern = "abba", str = "dog cat cat fish" should return false.
    pattern = "aaaa", str = "dog cat cat dog" should return false.
    pattern = "abba", str = "dog dog dog dog" should return false.

Notes:
- You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

## Method:

similar as [205: Isomorphic Strings](/hash/Isomorphic_Strings.md)

    class Solution(object):
        def wordPattern(self, pattern, str):
            """
            :type pattern: str
            :type str: str
            :rtype: bool
            """
            d1, d2=collections.defaultdict(int), collections.defaultdict(int)
            s=str.split()
            for i in range(len(pattern)):
                if (pattern[i] in d1) ^ (s[i] in d2) or len(pattern)!=len(s):
                    return False
                if d1[pattern[i]]!=d2[s[i]]:
                    return False
                d1[pattern[i]]=d2[s[i]]=i
            return True if pattern else False
            
len(set):

    class Solution(object):
        def wordPattern(self, pattern, str):
            """
            :type pattern: str
            :type str: str
            :rtype: bool
            """
            s=str.split()
            return len(pattern)==len(s) and len(set(zip(pattern, s)))==len(set(pattern))==len(set(s))