# 056. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

## Method:

Definition for an interval:

    class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

>type intervals: List[Interval]

To loop the list, we can use:
    
    for interval in intervals:
        interval.start...
        interval.end...
        
but we cannot loop it using the index:

    for i in range(len(intervals)-1):
        if intervals[i].end>=intervals[i+1].start
        ...
>AttributeError: 'list' object has no attribute 'end'.

## Solution:

使用双指针，一个遍历，一个与之比较并添加到结果集合中：

    # Definition for an interval.
    class Interval(object):
        def __init__(self, s=0, e=0):
            self.start = s
            self.end = e
    
    class Solution(object):
        def merge(self, intervals):
            """
            :type intervals: List[Interval]
            :rtype: List[Interval]
            """
            if not intervals:
                return []
            intervals.sort(key=lambda x: x.start)
            res=[intervals[0]]
            for i in intervals[1:]:
                if i.start<=res[-1].end:
                    res[-1].end=max(i.end,res[-1].end)
                else:
                    res.append(i)
            return res


