# 805. Split Array With Same Average

In a given integer array A, we must move every element of A to either list B or list C. (B and C initially start empty.)

Return true if and only if after such a move, it is possible that the average value of B is equal to the average value of C, and B and C are both non-empty.

Example :

    Input: 
    [1,2,3,4,5,6,7,8]
    Output: true
    Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have the average of 4.5.

Note:

- The length of A will be in the range [1, 30].
- A[i] will be in the range of [0, 10000].

## Method:

find i elements sum to ave*i, total of $2^i$ choices, using backtracking, tle:

    class Solution(object):
        def splitArraySameAverage(self, A):
            """
            :type A: List[int]
            :rtype: bool
            """
            s, l=sum(A), len(A)
            for i in range(1, l/2+1):
                if s*i%l==0 and self.checkSum(s*i/l, i, 0, 0, 0, A):
                    return True
            return False
        
        def checkSum(self, s, num, curSum, curNum, idx, A):
            if curSum==s and curNum==num:
                return True
            if curSum>s or curNum==num or idx==len(A):
                return False
            return self.checkSum(s, num, curSum+A[idx], curNum+1, idx+1, A) or self.checkSum(s, num, curSum, curNum, idx+1, A)
            
memo is needed, using dp knapsack, still tle (wtf???):

    class Solution(object):
        def splitArraySameAverage(self, A):
            """
            :type A: List[int]
            :rtype: bool
            """
            s, l=sum(A), len(A)
            dp=[[False]*(s+1) for _ in range(l/2+1)]
            dp[0][0]=True
            d={(0, 0):[]}
            for i in range(1, len(dp)):
                for idx in range(len(A)):
                    for j in range(len(dp[0])-1, -1, -1):
                        if dp[i-1][j] and j+A[idx]<len(dp[0]) and idx not in d[(i-1, j)]:
                            dp[i][j+A[idx]]=True
                            d[(i, j+A[idx])]=d[(i-1, j)]+[idx]
                if s*i%l==0 and dp[i][s*i/l]:
                    return True
            return False
            
## Solution:

backtracking with memo, still working on the memo part:

    class Solution(object):
        def splitArraySameAverage(self, A):
            """
            :type A: List[int]
            :rtype: bool
            """
            def find(target, num, idx):
                if (target, num) in not_found and not_found[(target, num)]<=idx:
                    return False
                if num==0: 
                    return target==0
                if idx==len(A): 
                    return False
                res=find(target-A[idx], num-1, idx+1) or find(target, num, idx+1)
                if not res: 
                    not_found[(target, num)]=min(not_found.get((target, num), n), idx)
                return res
            
            not_found={}
            n, s=len(A), sum(A)
            return any(find(s*i/n, i, 0) for i in range(1, n/2+1) if s*i%n==0)