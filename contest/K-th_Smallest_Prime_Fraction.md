# 786. K-th Smallest Prime Fraction

A sorted list A contains 1, plus some number of primes.  Then, for every p < q in the list, we consider the fraction p/q.

What is the K-th smallest fraction considered?  Return your answer as an array of ints, where answer[0] = p and answer[1] = q.

Examples:

    Input: A = [1, 2, 3, 5], K = 3
    Output: [2, 5]
    Explanation:
    The fractions to be considered in sorted order are:
    1/5, 1/3, 2/5, 1/2, 3/5, 2/3.
    The third fraction is 2/5.

    Input: A = [1, 7], K = 1
    Output: [1, 7]

Note:

- A will have length between 2 and 2000.
- Each A[i] will be between 1 and 30000.
- K will be between 1 and A.length * (A.length + 1) / 2.

## Method:

O(nK), tle:

    class Solution(object):
        def kthSmallestPrimeFraction(self, A, K):
            """
            :type A: List[int]
            :type K: int
            :rtype: List[int]
            """
            idx=[0]*len(A)
            res=0
            while K:
                m, i=float('inf'), 0
                for j in range(len(A)-1, 0, -1):
                    if A[idx[j]]*1.0/A[j]<m:
                        m=A[idx[j]]*1.0/A[j]
                        index=j
                    if j<len(A)-1 and idx[j]==idx[j+1]==idx[0]:
                        break
                res=index
                idx[index]+=1
                K-=1
            return [A[idx[res]-1], A[res]]
            
some modification based on above using heap, still tle:

    class Solution(object):
        def kthSmallestPrimeFraction(self, A, K):
            """
            :type A: List[int]
            :type K: int
            :rtype: List[int]
            """
            hp=[(A[0]*1.0/A[i], 0, i) for i in range(len(A))]
            heapq.heapify(hp)
            for i in range(K):
                value, index, base=heapq.heappop(hp)
                if index+1<len(A):
                    heapq.heappush(hp, (A[index+1]*1.0/A[base], index+1, base))
            return [A[index], A[base]]
            
binary search:

    class Solution(object):
        def kthSmallestPrimeFraction(self, A, K):
            """
            :type A: List[int]
            :type K: int
            :rtype: List[int]
            """
            lo, hi=A[0]*1.0/A[-1], float('-inf')
            for i in range(1, len(A)):
                hi=max(hi, A[i-1]*1.0/A[i])
            error=1e-9
            while hi-lo>error:
                mid=(lo+hi)/2
                count=0
                j=0
                for i in range(1, len(A)):
                    while j<i and A[j]*1.0/A[i]<=mid:
                        j+=1
                    count+=j
                if count>=K:
                    hi=mid
                else:
                    lo=mid
            s=set(A)
            for num in A:
                if round(lo*num, 4) in s:
                    return [int(round(lo*num, 4)), num]