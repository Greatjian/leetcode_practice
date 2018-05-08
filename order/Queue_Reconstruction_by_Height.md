# 406. Queue Reconstruction by Height

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
- The number of people is less than 1,100.


Example:

    Input:
    [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    
    Output:
    [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
    
## Method:

O(n^2), tle:

    class Solution(object):
        def reconstructQueue(self, people):
            """
            :type people: List[List[int]]
            :rtype: List[List[int]]
            """
            cnt=[people[i][1] for i in range(len(people))]
            res=[]
            for i in range(len(people)):
                idx, val=0, float('inf')
                for i in range(len(people)):
                    if cnt[i]==0 and people[i][0]<val:
                        val=people[i][0]
                        idx=i
                res.append(people[idx])
                for i in range(len(people)):
                    if people[i][0]<=val:
                        cnt[i]-=1
            return res
            
## Solution:

sort, O(nlogn):

    class Solution(object):
        def reconstructQueue(self, people):
            """
            :type people: List[List[int]]
            :rtype: List[List[int]]
            """
            people.sort(key=lambda p: (-p[0], p[1]))
            queue = []
            for p in people:
                queue.insert(p[1], p)
            return queue