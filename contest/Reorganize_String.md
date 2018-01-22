# 767. Reorganize String

Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

    Input: S = "aab"
    Output: "aba"

Example 2:

    Input: S = "aaab"
    Output: ""

Note:

- S will consist of lowercase letters and have length in range [1, 500].

## Method:

慢，但是通过了：

    class Solution(object):
        def reorganizeString(self, S):
            """
            :type S: str
            :rtype: str
            """
            d=collections.Counter(S)
            res=[]
            for _ in range(len(d.keys())):
                for k in d.keys():
                    if d[k]==min(d.values()):
                        for i in range(d[k]):
                            res.insert(2*i, k)
                        d[k]=max(d.values())+1
                        break
            for i in range(len(res)-1):
                if res[i]==res[i+1]:
                    return ""
            return "".join(res)

## Solution:

heap，防止重复增加cur:

    class Solution(object):
        def reorganizeString(self, S):
            """
            :type S: str
            :rtype: str
            """
            d=collections.Counter(S)
            pq=[]
            for (k, v) in d.items():
                heapq.heappush(pq, (-v, k))
            res=''
            cur=(0, '')
            while pq:
                v, k=heapq.heappop(pq)
                res+=k
                v+=1
                if cur[0]<0:
                    heapq.heappush(pq, cur)
                cur=(v, k)
            return res if len(res)==len(S) else ""
            
heap防止重复也可以一次pop两个：

    class Solution(object):
        def reorganizeString(self, S):
            """
            :type S: str
            :rtype: str
            """
            pq = [(-S.count(x), x) for x in set(S)]
            heapq.heapify(pq)
            if any(-nc > (len(S) + 1) / 2 for nc, x in pq):
                return ""
    
            ans = ""
            while len(pq) >= 2:
                v1, k1=heapq.heappop(pq)
                v2, k2=heapq.heappop(pq)
                ans+=k1+k2
                if v1<-1:
                    heapq.heappush(pq, (v1+1, k1))
                if v2<-1:
                    heapq.heappush(pq, (v2+1, k2))
            return ans+(pq[0][1] if pq else "")