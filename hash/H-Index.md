# 274. H-Index

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

    For example, 
    given citations = [3, 0, 6, 1, 5], 
    which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. 
    Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, 
    his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.

## Method:

dp, O(n2) slow:

    class Solution(object):
        def hIndex(self, citations):
            """
            :type citations: List[int]
            :rtype: int
            """
            if not citations:
                return 0
            res=[0]*(max(citations)+1)
            for c in citations:
                for j in range(c+1):
                    res[j]+=1
            count=0
            for i in range(len(res)):
                if res[i]>=i:
                    count=i
            return count

## Solution:

sort(), O(nlogn):

    class Solution(object):
        def hIndex(self, citations):
            """
            :type citations: List[int]
            :rtype: int
            """
            citations.sort()
            n = len(citations)
            for i in range(n):
                if citations[i]>=n-i:
                    return n-i
            return 0
            
bucket sort, O(n):

    class Solution(object):
        def hIndex(self, citations):
            """
            :type citations: List[int]
            :rtype: int
            """
            l=len(citations)
            res=[0]*(l+1)
            for c in citations:
                if c<=l:
                    res[c]+=1
                else:
                    res[l]+=1
            count=0
            for i in range(len(res)-1, -1, -1):
                count+=res[i]
                if count>=i:
                    return i
            return 0
                