# 788. Rotated Digits

X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X. A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:

    Input: 10
    Output: 4

Explanation: 
- There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
- Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

Note:

- N  will be in range [1, 10000].

## Method:

O(N*size(N)):

    class Solution(object):
        def rotatedDigits(self, N):
            """
            :type N: int
            :rtype: int
            """
            return sum(self.isGood(i) for i in range(1, N+1))
            
        def isGood(self, N):
            flag=False
            l=list(map(int, str(N)))
            for i in l:
                if i in [3,4,7]:
                    return 0
                if i in [2,5,6,9]:
                    flag=True
            return 1 if flag else 0
                