# 14. Longest Common Prefix


Write a function to find the longest common prefix string amongst an array of strings.

## Method:

    class Solution(object):
        def longestCommonPrefix(self, strs):
            """
            :type strs: List[str]
            :rtype: str
            """
            res=''
            if not strs:
                return ''
            i=0
            for s in strs[0]:
                for j in strs:
                    if len(j)==i or j[i]!=s:
                        return res
                i+=1
                res+=s
            return res
            
改写：min(strs, key=len)

    class Solution(object):
        def longestCommonPrefix(self, strs):
            """
            :type strs: List[str]
            :rtype: str
            """
            if not strs:
                return ''
            res=''
            s=min(strs, key=len)
            for i,v in enumerate(s):
                for j in strs:
                    if j[i]!=v:
                        return res
                res+=v
            return res
            
## Solution:

zip(*strs)

    class Solution(object):
        def longestCommonPrefix(self, strs):
            """
            :type strs: List[str]
            :rtype: str
            """
            res=''
            s=zip(*strs)
            for i in s:
                if len(set(i))>1:
                    return res
                res+=i[0]
            return res
