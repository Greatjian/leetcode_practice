# 447. Number of Boomerangs

Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:

    Input:
    [[0,0],[1,0],[2,0]]
    
    Output:
    2
    
    Explanation:
    The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

## Method:

只记录距离，not enough message, wrong ans:

    class Solution(object):
        def numberOfBoomerangs(self, points):
            """
            :type points: List[List[int]]
            :rtype: int
            """
            d=collections.defaultdict(int)
            for i in range(len(points)):
                for j in range(i+1, len(points)):
                    d[(points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2]+=1
            res=0
            for i in d.values():
                if i>2:
                    res+=2*i
                else:
                    res+=i*(i-1)
            return res
            
记录距离与位置, success:

    class Solution(object):
        def numberOfBoomerangs(self, points):
            """
            :type points: List[List[int]]
            :rtype: int
            """
            d1=collections.defaultdict(list)
            for i in range(len(points)):
                for j in range(len(points)):
                    d1[i].append((points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2)
            res=0
            for v in d1.values():
                d2=collections.Counter(v)
                res+=sum(i*(i-1) for i in d2.values())
            return res
            
## Solution:

记录位置可每一点新增字典实现：

    class Solution(object):
        def numberOfBoomerangs(self, points):
            """
            :type points: List[List[int]]
            :rtype: int
            """
            res=0
            for i in points:
                d=collections.defaultdict(int)
                for j in points:
                    distance=(i[0]-j[0])**2+(i[1]-j[1])**2
                    res+=2*d[distance]
                    d[distance]+=1
            return res