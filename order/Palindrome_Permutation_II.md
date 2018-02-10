# 267. Palindrome Permutation II

Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

    For example:
    
    Given s = "aabb", return ["abba", "baab"].
    
    Given s = "abc", return [].

## Method:

dfs, two many similar operation (e.g. "aaaaaaaaaaaaa"), tle:

    class Solution(object):
        def generatePalindromes(self, s):
            """
            :type s: str
            :rtype: List[str]
            """
            d=collections.Counter(s)
            odd, even=[], []
            for k in d.keys():
                if d[k]%2:
                    odd.append(k)
                    even+=[k]*(d[k]/2)
                else:
                    even+=[k]*(d[k]/2)
            if len(odd)>1:
                return []
            res=[]
            self.dfs(even, (odd[0] if odd else ''), '', res)
            return res
            
        def dfs(self, even, odd, path, res):
            if not even:
                path+=odd+path[::-1]
                if path not in res:
                    res.append(path)
                return
            for i in range(len(even)):
                self.dfs(even[:i]+even[i+1:], odd, path+even[i], res)
                
little modification, prevent same value:

    class Solution(object):
        def generatePalindromes(self, s):
            """
            :type s: str
            :rtype: List[str]
            """
            d=collections.Counter(s)
            odd, even=[], []
            for k in d.keys():
                if d[k]%2:
                    odd.append(k)
                    even+=[k]*(d[k]/2)
                else:
                    even+=[k]*(d[k]/2)
            if len(odd)>1:
                return []
            res=[]
            self.dfs(even, (odd[0] if odd else ''), '', res, [True]*len(even))
            return res
    
        def dfs(self, even, odd, path, res, flag):
            if not even:
                path+=odd+path[::-1]
                if path not in res:
                    res.append(path)
                return
            for i in range(len(even)):
                if i>0 and even[i]==even[i-1] and flag[i]:
                    continue
                flag[i]=False
                self.dfs(even[:i]+even[i+1:], odd, path+even[i], res, flag)
                flag[i]=True
                
## Solution:

using dictionary rather than list to store same key:

    class Solution(object):
        def generatePalindromes(self, s):
            """
            :type s: str
            :rtype: List[str]
            """
            d=collections.Counter(s)
            if sum(1 for i in d.values() if i%2)>1:
                return []
            res=[]
            odd=''
            for k in d.keys():
                if d[k]%2:
                    odd=k
                    d[k]-=1
                    break
            self.dfs(odd, '', res, d)
            return res
            
        def dfs(self, odd, path, res, d):
            if not any(d.values()):
                path+=odd+path[::-1]
                res.append(path)
                return
            for k in d.keys():
                if d[k]:
                    d[k]-=2
                    self.dfs(odd, path+k, res, d)
                    d[k]+=2