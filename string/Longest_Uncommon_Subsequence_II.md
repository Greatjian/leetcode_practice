# 522. Longest Uncommon Subsequence II

Given a list of strings, you need to find the longest uncommon subsequence among them. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

Example 1:

    Input: "aba", "cdc", "eae"
    Output: 3

Note:
- All the given strings' lengths will not exceed 10.
- The length of the given list will be in the range of [2, 50].

## Method:

wrong for case ["aaa","aaa","aa"], should be -1 instead of 2:

    class Solution(object):
        def findLUSlength(self, strs):
            """
            :type strs: List[str]
            :rtype: int
            """
            s=sorted(strs, key=len)
            if len(strs)==1:
                return len(strs[0])
            if s[-1]!=s[-2]:
                return len(s[-1])
            for i in range(len(s)-2, 0, -1):
                if s[i]!=s[i+1] and s[i]!=s[i-1]:
                    return len(s[i])
            if s[0]!=s[1]:
                return len(s[0])
            return -1
           
调整，但subsequence定义不准，wrong for ["aabbcc", "aabbcc","cb","abc"], should be 2 instead of 3：

    class Solution(object):
        def findLUSlength(self, strs):
            """
            :type strs: List[str]
            :rtype: int
            """
            s=sorted(strs, key=len)
            if len(strs)==1:
                return len(strs[0])
            if s[-1]!=s[-2]:
                return len(s[-1])
            for i in range(len(s)-2, 0, -1):
                if s[i]!=s[i+1] and s[i]!=s[i-1] and all(s[i] not in y for y in s[i+1:]):
                    return len(s[i])
            if s[0]!=s[1] and all(s[0] not in y for y in s[1:]):
                return len(s[0])
            return -1
            
调整，重写subsequence method，但排序有误, wrong for ["a","b","c","d","e","f","a","b","c","d","e","f"], should be -1 instead of 1:

    class Solution(object):
        def findLUSlength(self, strs):
            """
            :type strs: List[str]
            :rtype: int
            """
            s=sorted(strs, key=len)
            if len(strs)==1:
                return len(strs[0])
            if s[-1]!=s[-2]:
                print s
                return len(s[-1])
            for i in range(len(s)-2, 0, -1):
                if s[i]!=s[i+1] and s[i]!=s[i-1] and all(not self.sub(s[i], y) for y in s[i+1:]):
                    return len(s[i])
            if s[0]!=s[1] and all(not self.sub(s[0], y) for y in s[1:]):
                return len(s[0])
            return -1
            
        def sub(self, a, b):
            i=0
            for j in b:
                if i<len(a) and a[i]==j:
                    i+=1
            return i==len(a)
            
## Solution:

checking for subsequence should apply to all elements in the list:

    class Solution(object):
        def findLUSlength(self, strs):
            """
            :type strs: List[str]
            :rtype: int
            """
            s=sorted(strs, key=len)
            for i in range(len(s)-1, -1, -1):
                if all(not self.sub(s[i], y) for y in s[:i]+s[i+1:]):
                    return len(s[i])
            return -1
            
        def sub(self, a, b):
            i=0
            for j in b:
                if i<len(a) and a[i]==j:
                    i+=1
            return i==len(a)