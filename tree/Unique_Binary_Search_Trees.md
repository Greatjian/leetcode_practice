# 96. Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
    
    Given n = 3, there are a total of 5 unique BST's.
    
       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3
       
## Method:

root.left.val < root.val < root.right.val

记a[i]为i个元素能够构成BST的个数，则

>a[2]=a[0]*a[1]+a[1]*a[0]
>a[3]=a[0]*a[2]+a[1]*a[1]+a[2]*a[0]
>
>...
>
>a[n]=a[0]*a[n-1]+a[1]*a[n-2]+...+a[n-1]*a[0]

使用dp:

    class Solution(object):
        def numTrees(self, n):
            """
            :type n: int
            :rtype: int
            """
            dp=[0]*(n+1)
            dp[0]=1
            for i in range(n+1):
                for j in range(i):
                    dp[i]+=dp[j]*dp[i-1-j]
            return dp[-1]

