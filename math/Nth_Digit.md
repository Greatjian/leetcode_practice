# 400. Nth Digit

Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
- n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

    Input:
    3
    
    Output:
    3

Example 2:

    Input:
    11
    
    Output:
    0

Explanation:

    The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.

## Method:

逐级递减：

    class Solution(object):
        def findNthDigit(self, n):
            """
            :type n: int
            :rtype: int
            """
            digit=1
            length=9
            while n>digit*length:
                n-=digit*length
                digit+=1
                length*=10
            count, mod=10**(digit-1)+n/digit, n%digit
            return count/(10**(digit-mod))%10 if n%digit else (count-1)%10
            
## Solution:

n变为n-1后return不用分类：

    class Solution(object):
        def findNthDigit(self, n):
            """
            :type n: int
            :rtype: int
            """
            digit=1
            length=9
            while n>digit*length:
                n-=digit*length
                digit+=1
                length*=10
            count, mod=10**(digit-1)+(n-1)/digit, (n-1)%digit
            return int(str(count)[mod])