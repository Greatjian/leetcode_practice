# 796. Rotate String

We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:

    Input: A = 'abcde', B = 'cdeab'
    Output: true

Example 2:

    Input: A = 'abcde', B = 'abced'
    Output: false

Note:

- A and B will have length at most 100.

## Method:

O(n^2) brute force:

    class Solution(object):
        def rotateString(self, A, B):
            """
            :type A: str
            :type B: str
            :rtype: bool
            """
            for i in range(len(A)):
                if A[i]==B[0] and B==A[i:]+A[:i]:
                    return True
            return False
            
## Solution:

O(n):

    class Solution(object):
        def rotateString(self, A, B):
            """
            :type A: str
            :type B: str
            :rtype: bool
            """
            return len(A)==len(B) and B in A+A