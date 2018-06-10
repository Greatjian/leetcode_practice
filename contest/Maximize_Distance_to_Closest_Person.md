# 849. Maximize Distance to Closest Person

In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to closest person.

Example 1:

    Input: [1,0,0,0,1,0,1]
    Output: 2
    Explanation: 
    If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
    If Alex sits in any other open seat, the closest person has distance 1.
    Thus, the maximum distance to the closest person is 2.

Example 2:

    Input: [1,0,0,0]
    Output: 3
    Explanation: 
    If Alex sits in the last seat, the closest person is 3 seats away.
    This is the maximum distance possible, so the answer is 3.

Note:

- 1 <= seats.length <= 20000
- seats contains only 0s or 1s, at least one 0, and at least one 1.

## Method:

traditional three passes:

    class Solution(object):
        def maxDistToClosest(self, seats):
            """
            :type seats: List[int]
            :rtype: int
            """
            l=len(seats)
            left=[0]*l
            right=[0]*l
            for i in range(l):
                if seats[i]:
                    left[i]=0
                else:
                    left[i]=(left[i-1]+1 if i else float('inf'))
            for i in range(l-1, -1, -1):
                if seats[i]:
                    right[i]=0
                else:
                    right[i]=(right[i+1]+1 if i!=l-1 else float('inf'))
            res=0
            for i in range(l):
                res=max(res, min(left[i], right[i]))
            return res
            
## Solution:

One pass O(1) space:

    class Solution(object):
        def maxDistToClosest(self, seats):
            """
            :type seats: List[int]
            :rtype: int
            """
            l=len(seats)
            res=0
            i=0
            while i<l:
                while i<l and seats[i]==1:
                    i+=1
                j=i
                while j<l and seats[j]==0:
                    j+=1
                if i==0 or j==l:
                    res=max(res, j-i)
                else:
                    res=max(res, (j-i+1)/2)
                i=j
            return res