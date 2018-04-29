# 826. Most Profit Assigning Work

We have jobs: difficulty[i] is the difficulty of the ith job, and profit[i] is the profit of the ith job. 

Now we have some workers. worker[i] is the ability of the ith worker, which means that this worker can only complete a job with difficulty at most worker[i]. 

Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if 3 people attempt the same job that pays $1, then the total profit will be $3.  If a worker cannot complete any job, his profit is $0.

What is the most profit we can make?

Example 1:

    Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
    Output: 100 
    Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get profit of [20,20,30,30] seperately.

Notes:

- 1 <= difficulty.length = profit.length <= 10000
- 1 <= worker.length <= 10000
- difficulty[i], profit[i], worker[i]  are in range [1, 10^5]

## Method:

    class Solution(object):
        def maxProfitAssignment(self, difficulty, profit, worker):
            """
            :type difficulty: List[int]
            :type profit: List[int]
            :type worker: List[int]
            :rtype: int
            """
            res=[[difficulty[i], profit[i]] for i in range(len(profit))]
            res.sort(key=lambda i:i[0])
            dp=[0]*100001
            maxPro=0
            for i in range(len(res)):
                maxPro=max(maxPro, res[i][1])
                dp[res[i][0]]=maxPro
            for i in range(len(dp)):
                if i!=0 and dp[i]==0:
                    dp[i]=dp[i-1]
            return sum(dp[w] for w in worker)
            
## Solution:

save space, use more time (theoretically), here no (1057->183):

    class Solution(object):
        def maxProfitAssignment(self, difficulty, profit, worker):
            """
            :type difficulty: List[int]
            :type profit: List[int]
            :type worker: List[int]
            :rtype: int
            """
            res=[[difficulty[i], profit[i]] for i in range(len(profit))]
            res.sort(key=lambda i:i[0])
            worker.sort()
            cnt=0
            idx=0
            maxPro=0
            for i in range(len(worker)):
                while idx<len(res) and res[idx][0]<=worker[i]:
                    maxPro=max(maxPro, res[idx][1])
                    idx+=1
                cnt+=maxPro
            return cnt