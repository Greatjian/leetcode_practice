# 646. Maximum Length of Pair Chain

You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

Example 1:

    Input: [[1,2], [2,3], [3,4]]
    Output: 2
    Explanation: The longest chain is [1,2] -> [3,4]

Note:
- The number of given pairs will be in the range [1, 1000].

## Method:
暴力dp，超时：

    class Solution(object):
        def findLongestChain(self, pairs):
            """
            :type pairs: List[List[int]]
            :rtype: int
            """
            pairs.sort()
            dp=[1]*len(pairs)
            for i in range(len(pairs)):
                for j in range(i,len(pairs)):
                    if pairs[j][0]>pairs[i][1]:
                        dp[j]=max(dp[j],dp[i]+1)
            return dp[-1]
            
## Solution:
greedy，根据数组后一位排序：

    class Solution(object):
        def findLongestChain(self, pairs):
            """
            :type pairs: List[List[int]]
            :rtype: int
            """
            pairs.sort(key=lambda x: x[1])
            last=[float('-inf'),float('-inf')]
            count=0
            for p in pairs:
                if p[0]>last[-1]:
                    count+=1
                    last=p
            return count