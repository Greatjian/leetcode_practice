# 313. Super Ugly Number

Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
1. 1 is a super ugly number for any given primes.
2. The given numbers in primes are in ascending order.
3. 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
4. The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

## Method:

pointer records the index of res that needs to be multiplied for each prime:

    class Solution(object):
        def nthSuperUglyNumber(self, n, primes):
            """
            :type n: int
            :type primes: List[int]
            :rtype: int
            """
            res=[float('inf')]*n
            res[0]=1
            pointer=[0]*len(primes)
            for i in range(1, len(res)):
                min_index=0
                for j in range(len(primes)):
                    if res[pointer[j]]*primes[j]<res[i]:
                        res[i]=res[pointer[j]]*primes[j]
                        min_index=j
                    elif res[pointer[j]]*primes[j]==res[i]:
                        pointer[j]+=1
                pointer[min_index]+=1
            return res[-1]
            
## Solution:

    class Solution(object):
        def nthSuperUglyNumber(self, n, primes):
            """
            :type n: int
            :type primes: List[int]
            :rtype: int
            """
            buf = [1]
            idx = [0] * len(primes)
            ugly = [0] * len(primes)
            for _ in range(n-1):
                umin = float('inf')
                for i in range(len(primes)):
                    ugly[i] = primes[i] * buf[idx[i]]
                    umin = min(umin, ugly[i])
                for i, u in enumerate(ugly):
                    if umin == u:
                        idx[i] += 1
                buf.append(umin)
            return buf[-1]
            
        
        def nthSuperUglyNumber(self, n, primes):
            """
            :type n: int
            :type primes: List[int]
            :rtype: int
            """
            idx = [0] * len(primes)
            ugly = [0] * n
            ugly[0] = 1
            for i in range(1, n):
                ugly[i] = float('inf')
                for j in range(len(primes)):
                    ugly[i] = min(ugly[i], primes[j] * ugly[idx[j]])
                for j in range(len(primes)):
                    if primes[j] * ugly[idx[j]] == ugly[i]:
                        idx[j] += 1
            return ugly[-1]
            
        
        def nthSuperUglyNumber(self, n, primes):
            """
            :type n: int
            :type primes: List[int]
            :rtype: int
            """
            ugly = [0] * n
            ugly[0] = 1
            heap = [(p, 1, p) for p in primes]
            for i in range(1, n):
                ugly[i] = heap[0][0]
                while heap[0][0] == ugly[i]:
                    val, idx, p = heappop(heap)
                    heappush(heap, (ugly[idx] * p, idx + 1, p))
            return ugly[-1]