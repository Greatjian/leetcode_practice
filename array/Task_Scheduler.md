# 621. Task Scheduler

Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:

    Input: tasks = ['A','A','A','B','B','B'], n = 2
    Output: 8

Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

Note:
- The number of tasks is in the range [1, 10000].
- The integer n is in the range [0, 100].

## Method:
思路错误：按字母顺序做任务，出现次数多的先做，依次类推：

错误例子：

> ['A','A','A','A','A','A','B','C','D','E','F','G'], 2
>
> Output: 20
>
> Expected: 16
>
> 56 / 64 test cases passed.

    class Solution(object):
        def leastInterval(self, tasks, n):
            """
            :type tasks: List[str]
            :type n: int
            :rtype: int
            """
            res=count=0
            cnt = collections.Counter(tasks)
            tmax = max(cnt.values())
            while tmax>0:
                for i in cnt:
                    if cnt[i]>0:
                        count+=1
                        cnt[i]-=1
                if max(cnt.values())!=0:
                    res+=max(n+1,count)
                else:
                    res+=count
                print res
                count=0
                tmax-=1
            return res
            
## Solution

贪心法，直接从最多任务元素开始排列：

    class Solution(object):
        def leastInterval(self, tasks, n):
            """
            :type tasks: List[str]
            :type n: int
            :rtype: int
            """
            task_counts = collections.Counter(tasks).values()
            m = max(task_counts)
            num = task_counts.count(m)
            return max(len(tasks), (m - 1) * (n + 1) + num)