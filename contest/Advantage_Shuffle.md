# 870. Advantage Shuffle

Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.

 

Example 1:

    Input: A = [2,7,11,15], B = [1,10,4,11]
    Output: [2,11,7,15]

Example 2:

    Input: A = [12,24,8,32], B = [13,25,32,11]
    Output: [24,32,8,12]
 

Note:

- 1 <= A.length = B.length <= 10000
- 0 <= A[i] <= 10^9
- 0 <= B[i] <= 10^9

## Method:

greedy using sorting:

    class Solution(object):
        def advantageCount(self, A, B):
            """
            :type A: List[int]
            :type B: List[int]
            :rtype: List[int]
            """
            d=collections.defaultdict(list)
            for i,v in enumerate(B):
                d[v].append(i)
            A.sort()
            B.sort()
            ia,ib=0,0
            res=[]
            ept=[]
            while ia<len(A):
                while ia<len(A) and A[ia]<=B[ib]:
                    ept.append(A[ia])
                    ia+=1
                if ia<len(A):
                    res.append(A[ia])
                    ia+=1
                    ib+=1
            res+=ept
            newres=[-1]*len(A)
            for i in range(len(res)):
                newres[d[B[i]][-1]]=res[i]
                d[B[i]].pop()
            return newres
            
## Solution:

same idea, but more concise by sorting with index together:

    class Solution(object):
        def advantageCount(self, A, B):
            """
            :type A: List[int]
            :type B: List[int]
            :rtype: List[int]
            """
            B=[(v, i) for i, v in enumerate(B)]
            A.sort()
            B.sort()
            queue=collections.deque()
            res=[-1]*len(A)
            idx=0
            for v, i in B:
                while idx<len(A) and A[idx]<=v:
                    queue.append(A[idx])
                    idx+=1
                if idx<len(A):
                    res[i]=A[idx]
                    idx+=1
                else:
                    res[i]=queue.popleft()
            return res