# 862. Shortest Subarray with Sum at Least K

Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1. 

Example 1:

    Input: A = [1], K = 1
    Output: 1

Example 2:

    Input: A = [1,2], K = 4
    Output: -1

Example 3:

    Input: A = [2,-1,2], K = 3
    Output: 3
 

Note:

- 1 <= A.length <= 50000
- -10 ^ 5 <= A[i] <= 10 ^ 5
- 1 <= K <= 10 ^ 9

## Solution:

preSum for contiguous subarray, O(n^2) TLE:

    class Solution(object):
        def shortestSubarray(self, A, K):
            """
            :type A: List[int]
            :type K: int
            :rtype: int
            """
            preSum=[0]
            for i in A:
                preSum.append(preSum[-1]+i)
                
            def possible(l):
                for i in range(l, len(preSum)):
                    if preSum[i]-preSum[i-l]>=K:
                        return True
                return False
            
            for i in range(1, len(A)+1):
                if possible(i):
                    return i
            return -1
            
try binary search, but not applicable here:

    class Solution(object):
        def shortestSubarray(self, A, K):
            """
            :type A: List[int]
            :type K: int
            :rtype: int
            """
            preSum=[0]
            for i in A:
                preSum.append(preSum[-1]+i)
                
            def possible(l):
                for i in range(l, len(preSum)):
                    if preSum[i]-preSum[i-l]>=K:
                        return True
                return False
            
            lo, hi=1, len(A)
            while lo<hi:
                mid=(lo+hi)/2
                if possible(mid):
                    hi=mid
                else:
                    lo=mid+1
            if lo!=len(A):
                return lo
            for i in range(1, len(A)+1):
                if possible(i):
                    return i
            return -1
            
## Solution:

one pass using deque:

- i<j, preSum[i]>preSum[j], i is not optimal, pop from right
- preSum[j]-preSum[i]>=k, compute the shortest distance j-i, then i is not optimal, pop from left


    class Solution(object):
        def shortestSubarray(self, A, K):
            """
            :type A: List[int]
            :type K: int
            :rtype: int
            """
            preSum=[0]
            for a in A:
                preSum.append(a+preSum[-1])
            queue=collections.deque()
            res=len(A)+1
            for idx, val in enumerate(preSum):
                while queue and val<preSum[queue[-1]]:
                    queue.pop()
                while queue and val-preSum[queue[0]]>=K:
                    res=min(res, idx-queue.popleft())
                queue.append(idx)
            return res if res!=len(A)+1 else -1