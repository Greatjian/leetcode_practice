# 808. Soup Servings

There are two types of soup: type A and type B. Initially we have N ml of each type of soup. There are four kinds of operations:

- Serve 100 ml of soup A and 0 ml of soup B
- Serve 75 ml of soup A and 25 ml of soup B
- Serve 50 ml of soup A and 50 ml of soup B
- Serve 25 ml of soup A and 75 ml of soup B

When we serve some soup, we give it to someone and we no longer have it.  Each turn, we will choose from the four operations with equal probability 0.25. If the remaining volume of soup is not enough to complete the operation, we will serve as much as we can.  We stop once we no longer have some quantity of both types of soup.

Note that we do not have the operation where all 100 ml's of soup B are used first.  

Return the probability that soup A will be empty first, plus half the probability that A and B become empty at the same time.

Example:

    Input: N = 50
    Output: 0.625
    Explanation: 
    If we choose the first two operations, A will become empty first. For the third operation, A and B will become empty at the same time. For the fourth operation, B will become empty first. So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.

Notes:

- 0 <= N <= 10^9. 
- Answers within 10^-6 of the true value will be accepted as correct.

## Method:

wrong computation method:

    class Solution(object):
        def soupServings(self, N):
            """
            :type N: int
            :rtype: float
            """
            chance=1.0
            s=set([(N, N)])
            res=0.0
            while True:
                chance*=0.25
                ns=set()
                for i, j in s:
                    for a, b in [(100, 0), (75, 25), (50, 50), (25, 75)]:
                        if i>a and j>b:
                            ns.add((i-a, j-b))
                        elif i<=a and j<=b:
                            res+=chance*0.5
                        elif i<=a:
                            res+=chance
                s=ns
                if not s:
                    break
            return res
            
## Solution:

dp with trick for large N:

    class Solution(object):
        def soupServings(self, N):
            """
            :type N: int
            :rtype: float
            """
            def dfs(i, j):
                if i<=0 and j<=0:
                    return 0.5
                if i<=0:
                    return 1.0
                if j<=0:
                    return 0.0
                if (i, j) in d:
                    return d[(i, j)]
                d[(i, j)]=0.25*(dfs(i-100, j)+dfs(i-75, j-25)+dfs(i-50, j-50)+dfs(i-25, j-75))
                return d[(i, j)]
            
            d={}
            return dfs(N, N) if N<5000 else 1.0