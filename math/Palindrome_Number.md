## 009. Palindrome Number

Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
- Could negative integers be palindromes? (ie, -1)

- If you are thinking of converting the integer to string, note the restriction of using extra space.

- You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

- There is a more generic way of solving this problem.

## Method:

Using string (extra space):

    class Solution(object):
        def isPalindrome(self, x):
            """
            :type x: int
            :rtype: bool
            """
            return str(x)==str(x)[::-1]
            
## Solution:

similar to [Reverse Integer](/math/Reverse_Integer.md), but no need to check for overflow:

    class Solution(object):
        def isPalindrome(self, x):
            """
            :type x: int
            :rtype: bool
            """
            if x<0:
                return False
            temp=x
            y=0
            while x:
                y=y*10+x%10
                x/=10
            return y==temp