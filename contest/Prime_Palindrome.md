# 867. Prime Palindrome

Find the smallest prime palindrome greater than or equal to N.

Recall that a number is prime if it's only divisors are 1 and itself, and it is greater than 1. 

For example, 2,3,5,7,11 and 13 are primes.

Recall that a number is a palindrome if it reads the same from left to right as it does from right to left. 

For example, 12321 is a palindrome.

 

Example 1:

    Input: 6
    Output: 7

Example 2:

    Input: 8
    Output: 11

Example 3:

    Input: 13
    Output: 101
 

Note:

- 1 <= N <= 10^8
- The answer is guaranteed to exist and be less than 2 * 10^8.

## Method:

- Idea of functional programming is essential here.

- Tricky part is to get the next palindrome. Use four cases below 
(odd/even length, first half larger/smaller than second half):

> 2134->2222 --- head: 22 (=21+1)
>
> 3412->3443 --- head: 34
>
> 21534->21612 --- head: 216 (=215+1)
>
> 34512->34543 --- head: 345

    class Solution(object):
        def primePalindrome(self, N):
            """
            :type N: int
            :rtype: int
            """
            def isPrime(n):
                if n==2 or n==3: return True
                if n%2==0 or n<2: return False
                for i in range(3,int(n**0.5)+1,2):   # only odd numbers
                    if n%i==0:
                        return False    
                return True
            
            def next_palindrome(n):
                s = str(n)
                l = len(s)
                if s[:l//2][::-1] < s[(l+1)//2:]:
                    head = str(int(s[:(l+1)//2])+1)
                else:
                    head = s[:(l+1)//2]
                return int(head + head[:l//2][::-1])
    
            N=int(next_palindrome(N))
            while True:
                if isPrime(N):
                    return N
                N+=1
                N=int(next_palindrome(N))
