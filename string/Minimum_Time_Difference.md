# 539. Minimum Time Difference

Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.

Example 1:

    Input: ["23:59","00:00"]
    Output: 1

Note:
- The number of time points in the given list is at least 2 and won't exceed 20000.
- The input time is legal and ranges from 00:00 to 23:59.

## Method:

O(n2)超时:

    class Solution(object):
        def findMinDifference(self, timePoints):
            """
            :type timePoints: List[str]
            :rtype: int
            """
            a, b=[], []
            r=float('inf')
            for time in timePoints:
                a.append(int(time.split(':')[0]))
                b.append(int(time.split(':')[1]))
            for i in range(len(a)):
                for j in range(i+1, len(a)):
                    r=min(r, abs((a[i]-a[j])*60+b[i]-b[j]), 1440-abs((a[i]-a[j])*60+b[i]-b[j]))       
            return r
            
## Solution:

sort O(nlogn):

    class Solution(object):
        def findMinDifference(self, timePoints):
            """
            :type timePoints: List[str]
            :rtype: int
            """
            a=[]
            for time in timePoints:
                a.append(60 * int(time.split(':')[0]) + int(time.split(':')[1]))
            a.sort()
            r=float('inf')
            for i in range(len(a)):
                r=min(r, abs((a[i]-a[i-1])), 1440-abs(a[i]-a[i-1]))
            return r          