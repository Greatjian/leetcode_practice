# 356. Line Reflection

Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.

Example 1:

    Given points = [[1,1],[-1,1]], return true.

Example 2:

    Given points = [[1,1],[-1,-1]], return false.

Follow up:
- Could you do better than O(n2)?

## Method:

sorting using O(nlogn), careful for duplicates:

    class Solution(object):
        def isReflected(self, points):
            """
            :type points: List[List[int]]
            :rtype: bool
            """
            
            def check(l):
                s=l[len(l)/2]+l[(len(l)-1)/2]
                i, j=0, len(l)-1
                while i<j:
                    if l[i]+l[j]!=s:
                        return False, s
                    i+=1
                    j-=1
                return True, s
            
            d=collections.defaultdict(list)
            for x,y in points:
                d[y].append(x)
            s=None
            for y in d:
                d[y]=sorted(set(d[y]))
                b, news=check(d[y])
                if not b:
                    return False
                if s is not None and news!=s:
                    return False
                s=news
            return True
            
## Solution:

two-pass set O(n):

    class Solution(object):
        def isReflected(self, points):
            """
            :type points: List[List[int]]
            :rtype: bool
            """
            minX=float('inf')
            maxX=float('-inf')
            s=set()
            for x, y in points:
                minX=min(minX, x)
                maxX=max(maxX, x)
                s.add(str(x)+"a"+str(y))
            sum=minX+maxX
            for x, y in points:
                if str(sum-x)+"a"+str(y) not in s:
                    return False
            return True