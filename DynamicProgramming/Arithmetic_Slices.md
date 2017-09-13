# 413. Arithmetic Slices

A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

    For example, these are arithmetic sequence:

    1, 3, 5, 7, 9
    7, 7, 7, 7
    3, -1, -5, -9
    
The following sequence is not arithmetic.

    1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:

A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.


    Example:
    
    A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.

## Method:
每判断三数记录curr，再判断与之前是否相同增加至sum：

    class Solution(object):
        def numberOfArithmeticSlices(self, A):
            """
            :type A: List[int]
            :rtype: int
            """
            curr=sum=0
            for i in range(2,len(A)):
                if A[i]==2*A[i-1]-A[i-2]:
                    curr+=1
                    sum+=curr
                else:
                    curr=0
            return sum

## Solution:
前处的curr相当于遍历了这里dp，这里space O(n)不如上方法：

    class Solution(object):
        def numberOfArithmeticSlices(self, A):
            """
            :type A: List[int]
            :rtype: int
            """
            dp=[0]*len(A)
            sum=0
            for i in range(2,len(A)):
                if A[i]==2*A[i-1]-A[i-2]:
                    dp[i]=dp[i-1]+1
                    sum+=dp[i]
            return sum