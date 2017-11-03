# 049. Group Anagrams

Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

    [
      ["ate", "eat","tea"],
      ["nat","tan"],
      ["bat"]
    ]
    
## Method:

O(3)超时：

    class Solution(object):
        def groupAnagrams(self, strs):
            """
            :type strs: List[str]
            :rtype: List[List[str]]
            """
            ans=[]
            for s in strs:
                flag=1
                for i in range(len(ans)):
                    if sorted(s)==sorted(ans[i][0]):
                        ans[i].append(s)
                        flag=0
                        break
                if flag:
                    ans.append([s])
            return ans
            
dict():

    class Solution(object):
        def groupAnagrams(self, strs):
            """
            :type strs: List[str]
            :rtype: List[List[str]]
            """
            d={}
            for s in strs:
                s1=sorted(s)
                s2=tuple(s1)
                if s2 in d:
                    d[s2].append(s)
                else:
                    d[s2]=[s]
            return [v for v in d.values()]
            
## Solution:

    class Solution(object):
        def groupAnagrams(self, strs):
            """
            :type strs: List[str]
            :rtype: List[List[str]]
            """
            d=collections.defaultdict(list)
            for s in strs:
                s1=tuple(sorted(s))
                d[s1].append(s)
            return d.values()