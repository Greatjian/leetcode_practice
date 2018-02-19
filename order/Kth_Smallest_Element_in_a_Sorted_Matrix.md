# 378. Kth Smallest Element in a Sorted Matrix

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

    matrix = [
       [ 1,  5,  9],
       [10, 11, 13],
       [12, 13, 15]
    ],
    k = 8,
    
    return 13.

Note: 
- You may assume k is always valid, 1 ≤ k ≤ n2.

## Method:

pq:

    class Solution(object):
        def kthSmallest(self, matrix, k):
            """
            :type matrix: List[List[int]]
            :type k: int
            :rtype: int
            """
            m, n=len(matrix), len(matrix[0])
            pq=[(matrix[0][0], 0, 0)]
            visited=[[False]*n for _ in range(m)]
            visited[0][0]=True
            for i in range(k):
                value, i, j=heapq.heappop(pq)
                if i+1<m and not visited[i+1][j]:
                    visited[i+1][j]=True
                    heapq.heappush(pq, (matrix[i+1][j], i+1, j))
                if j+1<n and not visited[i][j+1]:
                    visited[i][j+1]=True
                    heapq.heappush(pq, (matrix[i][j+1], i, j+1))
            return value
            
binary search:

    class Solution(object):
        def kthSmallest(self, matrix, k):
            """
            :type matrix: List[List[int]]
            :type k: int
            :rtype: int
            """
            m, n=len(matrix), len(matrix[0])
            lo, hi=matrix[0][0], matrix[m-1][n-1]
            while lo<hi:
                mid=(lo+hi)/2
                j=n-1
                count=0
                for i in range(m):
                    while j>=0 and matrix[i][j]>mid:
                        j-=1
                    count+=j+1
                if count>k-1:
                    hi=mid
                else:
                    lo=mid+1
            return lo