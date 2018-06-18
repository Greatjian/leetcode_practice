# 854. K-Similar Strings

Strings A and B are K-similar (for some non-negative integer K) if we can swap the positions of two letters in A exactly K times so that the resulting string equals B.

Given two anagrams A and B, return the smallest K for which A and B are K-similar.

Example 1:

    Input: A = "ab", B = "ba"
    Output: 1

Example 2:

    Input: A = "abc", B = "bca"
    Output: 2

Example 3:

    Input: A = "abac", B = "baca"
    Output: 2

Example 4:

    Input: A = "aabc", B = "abca"
    Output: 2

Note:

- 1 <= A.length == B.length <= 20
- A and B contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}

## Method:

greedy, doesn't apply to the situation here:

    class Solution(object):
        def kSimilarity(self, A, B):
            """
            :type A: str
            :type B: str
            :rtype: int
            """
            if A==B:
                return 0
            db=collections.defaultdict(list)
            for i, v in enumerate(B):
                db[v].append(i)
            for i in range(len(B)):
                if B[i]!=A[i]:
                    break
            minval, minIdx=float('-inf'), -1
            for j in db[A[i]]:
                if j>i:
                    turn=self.check(A, B, i, j)
                    if turn>minval:
                        minval=turn
                        minIdx=j
            B=list(B)
            B[i], B[minIdx]=B[minIdx], B[i]
            B=''.join(B)
            return 1+self.kSimilarity(A, B)
                    
        def check(self, A, B, i, j):
            B=list(B)
            B[i], B[j]=B[j], B[i]
            return sum(A[i]==B[i] for i in range(len(A)))
            
brute force, append each digit and compare, 3997ms:

    class Solution(object):
        def kSimilarity(self, A, B):
            """
            :type A: str
            :type B: str
            :rtype: int
            """
            return self.helper(A, B)
        
        def helper(self, A, B):
            if B==A:
                return 0
            res=float('inf')
            for i in range(len(B)):
                if B[i]!=A[i]:
                    for j in range(i, len(B)):
                        if B[j]==A[i] and B[j]!=A[j]:
                            B=list(B)
                            B[i], B[j]=B[j], B[i]
                            B=''.join(B)
                            res=min(res, 1+self.helper(A, B))
                            B=list(B)
                            B[i], B[j]=B[j], B[i]
                            B=''.join(B)
                    break
            return res


## Solution:

add memorization, 383ms:

    class Solution(object):
        def kSimilarity(self, A, B):
            """
            :type A: str
            :type B: str
            :rtype: int
            """
            d={}
            return self.helper(A, B, d)
        
        def helper(self, A, B, d):
            if B==A:
                return 0
            if B in d:
                return d[B]
            res=float('inf')
            for i in range(len(B)):
                if B[i]!=A[i]:
                    for j in range(i, len(B)):
                        if B[j]==A[i] and B[j]!=A[j]:
                            B=list(B)
                            B[i], B[j]=B[j], B[i]
                            B=''.join(B)
                            res=min(res, 1+self.helper(A, B, d))
                            B=list(B)
                            B[i], B[j]=B[j], B[i]
                            B=''.join(B)   
                    break
            d[B]=res
            return res
            
similar idea with bfs:

    class Solution(object):
        def kSimilarity(self, A, B):
            """
            :type A: str
            :type B: str
            :rtype: int
            """
            s=set()
            queue=collections.deque([B])
            res=0
            while queue:
                for _ in range(len(queue)):
                    node=queue.popleft()
                    if node not in s:
                        s.add(node)
                        if node==A:
                            return res
                        i=0
                        while i<len(B) and node[i]==A[i]:
                            i+=1
                        for j in range(i+1, len(B)):
                            if node[j]==A[i] and node[j]!=A[j]:
                                queue.append(self.swap(node, i, j))
                res+=1
        
        def swap(self, B, i, j):
            B=list(B)
            B[i], B[j]=B[j], B[i]
            B=''.join(B)
            return B                  