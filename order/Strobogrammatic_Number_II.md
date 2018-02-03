# 247. Strobogrammatic Number II

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

    For example,
    Given n = 2, return ["11","69","88","96"].
    
## Method:

recursion, keep track of path:

    class Solution(object):
        def findStrobogrammatic(self, n):
            """
            :type n: int
            :rtype: List[str]
            """
            d={'0':'0','1':'1','6':'9','8':'8','9':'6'}
            res=[]
            
            def helper(lo, hi, path):
                if lo>hi:
                    res.append(''.join(path))
                    return
                if lo==hi:
                    for i in ['0','1','8']:
                        path[lo]=i
                        res.append(''.join(path))
                    return
                for i in d.keys():
                    path[lo]=i
                    path[hi]=d[i]
                    if not (lo==0 and i=='0'):
                        helper(lo+1, hi-1, path)
            
            helper(0, n-1, [0]*n)
            return res
            
## Solution:
            
直接return list可减少path:

    class Solution(object):
        def findStrobogrammatic(self, n):
            """
            :type n: int
            :rtype: List[str]
            """        
            def helper(n, m):
                if n==0:
                    return ['']
                if n==1:
                    return ['0','1','8']
                res=helper(n-2, m)
                newRes=[]
                for i in res:
                    if n!=m:
                        newRes.append('0'+i+'0')
                    newRes.append('1'+i+'1')
                    newRes.append('6'+i+'9')
                    newRes.append('8'+i+'8')
                    newRes.append('9'+i+'6')
                return newRes
            
            return helper(n, n)