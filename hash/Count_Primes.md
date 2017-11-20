# 204. Count Primes

Description:

Count the number of prime numbers less than a non-negative number, n.

## Method:

tle:

    class Solution(object):
        def countPrimes(self, n):
            """
            :type n: int
            :rtype: int
            """
            count=0
            for i in range(2, n):
                if self.isPrime(i):
                    count+=1
            return count        
            
        def isPrime(self, n):
            if n==2:
                return True
            if not n%2:
                return False
            for i in range(3, int(n**0.5)+1, 2):
                if not n%i:
                    return False
            return True
            
## Solution:

    class Solution(object):
        def countPrimes(self, n):
            """
            :type n: int
            :rtype: int
            """
            count=0
            isPrime=[1]*n
            if n<2:
                return 0
            isPrime[0]=isPrime[1]=0
            for i in range(2, n):
                if isPrime[i]:
                    j=2
                    while(i*j<n):
                        isPrime[i*j]=0
                        j+=1
            return sum(isPrime)
            
faster:

    class Solution(object):
        def countPrimes(self, n):
            """
            :type n: int
            :rtype: int
            """
            count=0
            isPrime=[1]*n
            if n<2:
                return 0
            isPrime[0]=isPrime[1]=0
            for i in range(2, int(n**0.5)+1):
                if isPrime[i]:
                    isPrime[i*i:n:i]=[0]*len(isPrime[i*i:n:i])
            return sum(isPrime)