# 265. Paint House II

There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
- All costs are positive integers.

Follow up:
- Could you solve it in O(nk) runtime?

## Method:

similar to last one, O(nk^2):

    class Solution(object):
        def minCostII(self, costs):
            """
            :type costs: List[List[int]]
            :rtype: int
            """
            if not costs:
                return 0
            n, k=len(costs), len(costs[0])
            for i in range(1, n):  
                for j in range(k):
                    m=float('inf')
                    for count in range(k):
                        if j==count:
                            continue
                        m=min(m, costs[i-1][count])
                    costs[i][j]+=m
            return min(costs[-1][i] for i in range(k))
            
## Solution:

only track min1 and min2 for each line, O(nk):

    class Solution(object):
        def minCostII(self, costs):
            """
            :type costs: List[List[int]]
            :rtype: int
            """
            if not costs:
                return 0
            n, k=len(costs), len(costs[0])
            for i in range(1, n): 
                min1=min(costs[i-1])
                idx=costs[i-1].index(min1)
                min2=min(costs[i-1][:idx]+costs[i-1][idx+1:])
                for j in range(k):
                    if j!=idx:
                        costs[i][j]+=min1
                    else:
                        costs[i][j]+=min2
            return min(costs[-1][i] for i in range(k))
            
O(1) space:

    class Solution(object):
        def minCostII(self, costs):
            """
            :type costs: List[List[int]]
            :rtype: int
            """
            if not costs:
                return 0
            n, k=len(costs), len(costs[0])
            min1, min2, index=0, 0, 0
            cost=0
            for i in range(n): 
                m1, m2, idx=float('inf'), float('inf'), -1
                for j in range(k):
                    costs[i][j]+=(min1 if j!=index else min2)
                    if costs[i][j]<m1:
                        m2=m1
                        m1=costs[i][j]
                        idx=j
                    elif costs[i][j]<m2:
                        m2=costs[i][j]
                min1, min2, index=m1, m2, idx
            return min1