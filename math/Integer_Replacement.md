# 397. Integer Replacement

Given a positive integer n and you can do operations as follow:

- If n is even, replace n with n/2.
- If n is odd, you can replace n with either n + 1 or n - 1.

What is the minimum number of replacements needed for n to become 1?

Example 1:

    Input:
    8
    
    Output:
    3

Explanation:

    8 -> 4 -> 2 -> 1

Example 2:

    Input:
    7
    
    Output:
    4

Explanation:

    7 -> 8 -> 4 -> 2 -> 1
    or
    7 -> 6 -> 3 -> 2 -> 1

## Method:

doing as much /2 as possible:

    class Solution(object):
        def integerReplacement(self, n):
            """
            :type n: int
            :rtype: int
            """
            count=0
            while n!=1:
                if n%2==0:
                    n/=2
                elif n%4==1 or n==3:
                    n-=1
                else:
                    n+=1
                count+=1
            return count
            
## Solution:

recursion+memorization:

    class Solution(object):
        def integerReplacement(self, n):
            """
            :type n: int
            :rtype: int
            """
            d={}
            return self.helper(n, d)
        
        def helper(self, n, d):
            if n in d:
                return d[n]
            if n==1:
                return 0
            if not n%2:
                d[n]=1+self.helper(n/2, d)
            else:
                d[n]=1+min(self.helper(n+1, d), self.helper(n-1, d))
            return d[n]