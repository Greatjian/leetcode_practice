# 149. Max Points on a Line

Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

    Input: [[1,1],[2,2],[3,3]]
    Output: 3
    Explanation:
    ^
    |
    |        o
    |     o
    |  o  
    +------------->
    0  1  2  3  4

Example 2:

    Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    Output: 4
    Explanation:
    ^
    |
    |  o
    |     o        o
    |        o
    |  o        o
    +------------------->
    0  1  2  3  4  5  6
    
## Method:

set to remove duplicates for (k, b) in a line

numpy.longdouble to add float precision

    # Definition for a point.
    # class Point(object):
    #     def __init__(self, a=0, b=0):
    #         self.x = a
    #         self.y = b
    import numpy as np
    class Solution(object):
        def maxPoints(self, points):
            """
            :type points: List[Point]
            :rtype: int
            """
            d1=collections.defaultdict(int)
            d2=collections.defaultdict(set)
            for p in points:
                d1[(p.x, p.y)]+=1
            for i in range(len(points)):
                for j in range(i+1, len(points)):
                    x1, y1, x2, y2=points[i].x,points[i].y,points[j].x,points[j].y
                    if x1==x2:
                        d2[("inf", x1)].add((x1,y1))
                        d2[("inf", x1)].add((x2,y2))
                    else:
                        k=(np.longdouble)(y2-y1)*1.0/(x2-x1)
                        b=(np.longdouble)(x2*y1-y2*x1)*1.0/(x2-x1)
                        d2[(k,b)].add((x1,y1))
                        d2[(k,b)].add((x2,y2))
            if not points:
                return 0
            if len(points)==1:
                return 1
            res=float('-inf')
            for k in d2:
                acc=0
                for v in d2[k]:
                    acc+=d1[v]
                res=max(res, acc)
            return res