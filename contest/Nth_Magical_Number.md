# 878. Nth Magical Number

A positive integer is magical if it is divisible by either A or B.

Return the N-th magical number.  Since the answer may be very large, return it modulo 10^9 + 7.

 

Example 1:

    Input: N = 1, A = 2, B = 3
    Output: 2

Example 2:

    Input: N = 4, A = 2, B = 3
    Output: 6

Example 3:

    Input: N = 5, A = 2, B = 4
    Output: 10

Example 4:

    Input: N = 3, A = 6, B = 4
    Output: 8
 

Note:

- 1 <= N <= 10^9
- 2 <= A <= 40000
- 2 <= B <= 40000

## Method:

use gcd to reduce to range of lcm(A, B), then maintain a heap of size remainder:

    class Solution(object):
        def nthMagicalNumber(self, N, A, B):
            """
            :type N: int
            :type A: int
            :type B: int
            :rtype: int
            """
            def gcd(a,b):     
                if b == 0:
                    return a
                remainder = a % b
                return gcd(b,remainder)
    
            def lcm(a, b):
                return int( (a*b) / gcd(a,b))
            
            C=lcm(A, B)
            cnt=C/A+C/B-1
            base=(C*(N/cnt))%(10**9+7)
            remain=N%cnt
            if remain==0:
                return base
            hp=[]
            for i in range(A, C, A):
                heapq.heappush(hp, -i)
                if len(hp)>remain:
                    heapq.heappop(hp)
                    break
            for i in range(B, C, B):
                heapq.heappush(hp, -i)
                if len(hp)>remain:
                    heapq.heappop(hp)
                    if i>-hp[0]:
                        break
            return (base-hp[0])%(10**9+7)
            
## Solution:

binary search for each count using lcm:

    class Solution(object):
        def nthMagicalNumber(self, N, A, B):
            """
            :type N: int
            :type A: int
            :type B: int
            :rtype: int
            """
            def gcd(a,b):     
                if b == 0:
                    return a
                remainder = a % b
                return gcd(b,remainder)
    
            def lcm(a, b):
                return int( (a*b) / gcd(a,b))
            
            def getNumber(num):
                cnt=0
                cnt+=num/A
                cnt+=num/B
                cnt-=num/C
                return cnt
            
            C=lcm(A, B)
            lo, hi=min(A, B), 10**32
            while lo<hi:
                mid=(lo+hi)/2
                if getNumber(mid)>=N:
                    hi=mid
                else:
                    lo=mid+1
            return lo%(10**9+7)