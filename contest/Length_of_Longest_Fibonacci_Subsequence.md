# 873. Length of Longest Fibonacci Subsequence

A sequence X_1, X_2, ..., X_n is fibonacci-like if:

- n >= 3
- X_i + X_{i+1} = X_{i+2} for all i + 2 <= n
- Given a strictly increasing array A of positive integers forming a sequence, find the length of the longest fibonacci-like subsequence of A.  If one does not exist, return 0.

(Recall that a subsequence is derived from another sequence A by deleting any number of elements (including none) from A, without changing the order of the remaining elements.  For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].)

 

Example 1:

    Input: [1,2,3,4,5,6,7,8]
    Output: 5
    Explanation:
    The longest subsequence that is fibonacci-like: [1,2,3,5,8].

Example 2:

    Input: [1,3,7,11,12,14,18]
    Output: 3
    Explanation:
    The longest subsequence that is fibonacci-like:
    [1,11,12], [3,11,14] or [7,11,18].
 

Note:

- 3 <= A.length <= 1000
- 1 <= A[0] < A[1] < ... < A[A.length - 1] <= 10^9
- (The time limit has been reduced by 50% for submissions in Java, C, and C++.)

## Method:

O(n^2logM) where M=max(A) brute force:

    class Solution(object):
        def lenLongestFibSubseq(self, A):
            """
            :type A: List[int]
            :rtype: int
            """
            s=set(A)
            res=0
            for i in range(len(A)):
                for j in range(i+1, len(A)):
                    cnt=2
                    a,b=A[i], A[j]
                    while True:
                        if a+b in s:
                            cnt+=1
                            a,b=b,a+b
                        else:
                            break
                    if cnt==2:
                        cnt=0
                    res=max(res, cnt)
            return res

## Solution:

O(n^2) using dp:

    class Solution(object):
        def lenLongestFibSubseq(self, A):
            """
            :type A: List[int]
            :rtype: int
            """
            d={}
            for i in range(len(A)):
                for j in range(i+1, len(A)):
                    if A[j]-A[i]>0 and (A[j]-A[i], A[i]) in d:
                        d[(A[i], A[j])]=d[(A[j]-A[i], A[i])]+1
                    else:
                        d[(A[i], A[j])]=2
            return max(d.values()) if max(d.values())!=2 else 0