# 218. The Skyline Problem

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).

Buildings  Skyline Contour

The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

- The number of buildings in any input list is guaranteed to be in the range [0, 10000].
- The input list is already sorted in ascending order by the left x position Li.
- The output list must be sorted by the x position.
- There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]

## Method:

heap for height:

t to record raise memory error:

    class Solution(object):
        def getSkyline(self, buildings):
            """
            :type buildings: List[List[int]]
            :rtype: List[List[int]]
            """
            if not buildings:
                return []
            res=[]
            t=max(b[1] for b in buildings)
            hp=[]
            m=0
            for i in range(t+1):
                for building in buildings:
                    if building[0]==i:
                        heapq.heappush(hp, (-building[2], building[0], building[1]))
                        if building[2]>m:
                            if res and i==res[-1][0] and building[2]>res[-1][-1]:
                                res[-1]=[i, building[2]]
                            else:
                                res.append([i, building[2]])
                            m=building[2]
                    if hp and hp[0][2]==i:
                        while hp and hp[0][2]<=i:
                            heapq.heappop(hp)
                        res.append([i, (-hp[0][0] if hp else 0)])
                        m=(hp[0][0] if hp else 0)
            return res
            
for loop not good enough:

    class Solution(object):
        def getSkyline(self, buildings):
            """
            :type buildings: List[List[int]]
            :rtype: List[List[int]]
            """
            if not buildings:
                return []
            hp=[]
            res=[]
            buildings.sort(key=lambda i: i[0])
            for b in buildings:
                if not hp or b[0]<hp[0][2]:
                    if not hp or b[2]>-1*hp[0][0]:
                        if res and b[0]==res[-1][0]:
                            res[-1][1]=b[2]
                        else:
                            res.append([b[0], b[2]])
                    heapq.heappush(hp, (-b[2], b[0], b[1]))
                else:
                    while hp and hp[0][2]<=b[0]:
                        end=hp[0][2]
                        heapq.heappop(hp)
                        while hp and hp[0][2]<=end:
                            heapq.heappop(hp)
                        res.append([end, (-hp[0][0] if hp else 0)])
                    heapq.heappush(hp, (-b[2], b[0], b[1]))
                    if res and b[0]==res[-1][0]:
                        res[-1][1]=-hp[0][0]
                    else:
                        res.append([b[0], -hp[0][0]])
            
            return res[:-1]                    
            
## Solution:

divide and conquer (merge):

    class Solution(object):
        def getSkyline(self, buildings):
            """
            :type buildings: List[List[int]]
            :rtype: List[List[int]]
            """
            res=[]
            buildings.sort(key=lambda i: i[0])
            for b in buildings:
                res.append([[b[0], b[2]],[b[1], 0]])
            return self.merge(res)
        
        def merge(self, res):
            if not res:
                return []
            if len(res)==1:
                return res[0]
            l=[]
            for i in range(len(res)/2):
                l.append(self.merge2(res[i*2], res[i*2+1]))
            if len(res)%2:
                l.append(res[-1])
            return self.merge(l)
        
        def merge2(self, l1, l2):
            h1, h2=0, 0
            i, j=0, 0
            res=[]
            while i<len(l1) and j<len(l2):
                if l1[i][0]==l2[j][0]:
                    h1, h2=l1[i][1], l2[j][1]
                    if not res or max(h1, h2)!=res[-1][-1]:
                        res.append([l1[i][0], max(h1, h2)])
                    i+=1
                    j+=1
                elif l1[i][0]<l2[j][0]:
                    h1=l1[i][1]
                    if not res or max(h1, h2)!=res[-1][-1]:
                        res.append([l1[i][0], max(h1, h2)])
                    i+=1
                else:
                    h2=l2[j][1]
                    if not res or max(h1, h2)!=res[-1][-1]:
                        res.append([l2[j][0], max(h1, h2)])
                    j+=1
            if i==len(l1):
                res+=l2[j:]
            else:
                res+=l1[i:]
            return res
            
stack:

while loop manipulates better; adding an eternal end point; edge cases consideration;
defensive coding (if not hp or hp[0].../while hp...hp.pop()):

    class Solution(object):
        def getSkyline(self, buildings):
            """
            :type buildings: List[List[int]]
            :rtype: List[List[int]]
            """
            if not buildings:
                return []
            hp=[]
            res=[]
            buildings.sort(key=lambda i: i[0])
            buildings.append([float('inf'), float('inf'), 0])
            i=0
            while i<len(buildings):
                if not hp or buildings[i][0]<=hp[0][2]:
                    x=buildings[i][0]
                    heapq.heappush(hp, (-buildings[i][2], buildings[i][0], buildings[i][1]))
                    i+=1
                    while i<len(buildings) and buildings[i][0]==buildings[i-1][0]:
                        heapq.heappush(hp, (-buildings[i][2], buildings[i][0], buildings[i][1]))
                        i+=1
                else:
                    x=hp[0][2]
                    while hp and hp[0][2]<=x:
                        heapq.heappop(hp)
                h=(-hp[0][0] if hp else 0)
                if not res or h!=res[-1][1]:
                    res.append([x, h])
            return res