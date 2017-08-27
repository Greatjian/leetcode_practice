# 279. Perfect Squares

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

## Solution:
1

    class Solution(object):
        _dp = [0]
        def numSquares(self, n):
            dp = self._dp
            while len(dp) <= n:
                dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
            return dp[n]
2

    class Solution(object):
        def numSquares(self, n):
            """
            :type n: int
            :rtype: int
            """
            if n < 2: 
                return n 
            lst = []
            i = 1 
            while i * i <= n: 
                lst.append(i*i)
                i += 1 
            cnt = 0
            toCheck = {n}
            while toCheck: 
                cnt += 1 
                temp = set()
                for x in toCheck: 
                    for y in lst: 
                        if x == y: 
                            return cnt 
                        if x < y: 
                            break 
                        temp.add(x-y)
                toCheck = temp 
            return cnt 