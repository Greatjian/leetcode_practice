# 253. Meeting Rooms II

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

    For example,
    Given [[0, 30],[5, 10],[15, 20]],
    return 2.

## Method:

    # Definition for an interval.
    # class Interval(object):
    #     def __init__(self, s=0, e=0):
    #         self.start = s
    #         self.end = e
    
    class Solution(object):
        def minMeetingRooms(self, intervals):
            """
            :type intervals: List[Interval]
            :rtype: int
            """
            intervals.sort(key=lambda x: x.start)
            res=[]
            for i in intervals:
                flag=True
                for j in range(len(res)):
                    if i.start>=res[j]:
                        res[j]=i.end
                        flag=False
                        break
                if flag:
                    res.append(i.end)
            return len(res)
            
## Solution:
            
sort using heap, faster:

    # Definition for an interval.
    # class Interval(object):
    #     def __init__(self, s=0, e=0):
    #         self.start = s
    #         self.end = e
    
    class Solution(object):
        def minMeetingRooms(self, intervals):
            """
            :type intervals: List[Interval]
            :rtype: int
            """
            intervals.sort(key=lambda x: x.start)
            hp=[]
            for i in intervals:
                if not hp or hp[0]>i.start:
                    heapq.heappush(hp, i.end)
                else:
                    heapq.heappop(hp)
                    heapq.heappush(hp, i.end)
            return len(hp)
            