# 829. Consecutive Numbers Sum

Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

Example 1:

    Input: 5
    Output: 2
    Explanation: 5 = 5 = 2 + 3

Example 2:

    Input: 9
    Output: 3
    Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4

Example 3:

    Input: 15
    Output: 4
    Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5

Note: 1 <= N <= 10 ^ 9.

## Method:

preSum, O(n), TLE (91/170):

    class Solution(object):
        def consecutiveNumbersSum(self, N):
            """
            :type N: int
            :rtype: int
            """
            dp=[i for i in range(N+1)]
            for i in range(1, len(dp)):
                dp[i]+=dp[i-1]
            cnt=0
            s=set()
            for i in dp:
                if i>=N and i-N in s:
                    cnt+=1
                s.add(i)
            #print dp, s
            return cnt
            
O(n**0.5):

s=1+2+...+i,
i=number of consecutive numbers

(21-6)%3==0 => (1+2+3) => (6+7+8)

    class Solution(object):
        def consecutiveNumbersSum(self, N):
            """
            :type N: int
            :rtype: int
            """
            cnt=0
            i=0
            s=0
            while s<N:
                i+=1
                s+=i
                if (N-s)%i==0:
                    cnt+=1
            return cnt
            
(even*(0.5\*odd)) or (odd\*integer), even/odd>(0.5\*odd/integer)/2:
            
    class Solution(object):
        def consecutiveNumbersSum(self, N):
            """
            :type N: int
            :rtype: int
            """
            cnt=0
            i=1
            while i<(N*2)**0.5:
                if N%i==0 and i%2:
                        cnt+=1
                if N%i!=0 and (N*1.0/i)%0.5==0 and i%2==0:
                    cnt+=1
                i+=1
            return cnt