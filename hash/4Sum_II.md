# 454. 4Sum II

Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

    Input:
    A = [ 1, 2]
    B = [-2,-1]
    C = [-1, 2]
    D = [ 0, 2]
    
    Output:
    2
    
    Explanation:
    The two tuples are:
    1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
    2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
    
## Method:

O(n2) tle:

    class Solution(object):
        def fourSumCount(self, A, B, C, D):
            """
            :type A: List[int]
            :type B: List[int]
            :type C: List[int]
            :type D: List[int]
            :rtype: int
            """
            d=collections.Counter(A)
            d1, d2, d3=collections.defaultdict(int), collections.defaultdict(int), collections.defaultdict(int)
            
            for i in d:
                for j in B:
                    d1[i+j]+=d[i]
    
            for i in d1:
                for j in C:
                    d2[i+j]+=d1[i]
            
            for i in d2:
                for j in D:
                    d3[i+j]+=d2[i]
                    
            return d3[0]
            
## Solution:

amazing...

    class Solution(object):
        def fourSumCount(self, A, B, C, D):
            """
            :type A: List[int]
            :type B: List[int]
            :type C: List[int]
            :type D: List[int]
            :rtype: int
            """
            dict = collections.Counter(a+b for a in A for b in B)
            return sum(dict[-c-d] for c in C for d in D)
            
复杂版：

    class Solution(object):
        def fourSumCount(self, A, B, C, D):
            """
            :type A: List[int]
            :type B: List[int]
            :type C: List[int]
            :type D: List[int]
            :rtype: int
            """
            dict = collections.defaultdict(int)
            res=0
            
            for a in A:
                for b in B:
                    dict[a+b]+=1
                    
            for c in C:
                for d in D:
                    res+=dict[-c-d]
                    
            return res