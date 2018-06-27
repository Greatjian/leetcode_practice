# 857. Minimum Cost to Hire K Workers

There are N workers.  The i-th worker has a quality[i] and a minimum wage expectation wage[i].

Now we want to hire exactly K workers to form a paid group.  When hiring a group of K workers, we must pay them according to the following rules:

- Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
- Every worker in the paid group must be paid at least their minimum wage expectation.

Return the least amount of money needed to form a paid group satisfying the above conditions.

 

Example 1:

    Input: quality = [10,20,5], wage = [70,50,30], K = 2
    Output: 105.00000
    Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.

Example 2:

    Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
    Output: 30.66667
    Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers seperately. 
 

Note:

- 1 <= K <= N <= 10000, where N = quality.length = wage.length
- 1 <= quality[i] <= 10000
- 1 <= wage[i] <= 10000
- Answers within 10^-5 of the correct answer will be considered correct.

## Method:

answer=max(ratio)*sum(top K quality)

1. sort with respect to ratio
2. compute top k while traversing the sorted list (heap)

without memorization, tle:

    class Solution(object):
        def mincostToHireWorkers(self, quality, wage, K):
            """
            :type quality: List[int]
            :type wage: List[int]
            :type K: int
            :rtype: float
            """
            ans=float('inf')
            res=[[quality[i], wage[i]] for i in range(len(quality))]
            res.sort(key=lambda i: i[1]*1.0/i[0])
            for i in range(K-1, len(res)):
                ans=min(ans, res[i][1]*sum(sorted([res[k][0] for k in range(i+1)])[:K])*1.0/res[i][0])
            return ans
            
## Solution:

    class Solution(object):
        def mincostToHireWorkers(self, quality, wage, K):
            """
            :type quality: List[int]
            :type wage: List[int]
            :type K: int
            :rtype: float
            """
            ans=float('inf')
            res=[[quality[i], wage[i]] for i in range(len(quality))]
            res.sort(key=lambda i: i[1]*1.0/i[0])
            pq=[]
            s=0
            for i in res:
                heapq.heappush(pq, -i[0])
                s+=i[0]
                if len(pq)>K:
                    s+=heapq.heappop(pq)
                if len(pq)==K:
                    ans=min(ans, i[1]*s*1.0/i[0])
            return ans
            