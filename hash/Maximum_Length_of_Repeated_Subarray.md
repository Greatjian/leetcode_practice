# 718. Maximum Length of Repeated Subarray

Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

    Input:
    A: [1,2,3,2,1]
    B: [3,2,1,4,7]
    Output: 3
    Explanation: 
    The repeated subarray with maximum length is [3, 2, 1].

Note:
- 1 <= len(A), len(B) <= 1000
- 0 <= A[i], B[i] < 100

## Method:

dp, O(m*n):

    class Solution(object):
        def findLength(self, A, B):
            """
            :type A: List[int]
            :type B: List[int]
            :rtype: int
            """
            dp=[[0]*(len(B)+1) for _ in range(len(A)+1)]
            ans=0
            for i in range(1, len(A)+1):
                for j in range(1, len(B)+1):
                    if A[i-1]==B[j-1]:
                        dp[i][j]=dp[i-1][j-1]+1
                        ans=max(ans, dp[i][j])
            return ans
            
or 

    class Solution(object):
        def findLength(self, A, B):
            """
            :type A: List[int]
            :type B: List[int]
            :rtype: int
            """
            dp=[[0]*(len(B)+1) for _ in range(len(A)+1)]
            for i in range(1, len(A)+1):
                for j in range(1, len(B)+1):
                    if A[i-1]==B[j-1]:
                        dp[i][j]=dp[i-1][j-1]+1
            return max(max(row) for row in dp)
            
## Solution:

length binary search: O((M+N)∗log(min(M,N))):

    class Solution(object):
        def findLength(self, A, B):
            """
            :type A: List[int]
            :type B: List[int]
            :rtype: int
            """
            if len(A) > len(B): 
                return findLength(B, A)
            
            def check(length):
                lookup = set(A[i:i+length] for i in range(len(A)-length+1))
                return any(B[j:j+length] in lookup for j in range(len(B)-length+1))
    
            A = ''.join(map(chr, A))
            B = ''.join(map(chr, B))
            left, right = 0, min(len(A), len(B)) + 1
            while left < right:
                mid = left + (right-left)/2
                if not check(mid):
                    right = mid
                else:
                    left = mid+1
            return left-1