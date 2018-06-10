# 850. Rectangle Area II

We are given a list of (axis-aligned) rectangles.  Each rectangle[i] = [x1, y1, x2, y2] , where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the ith rectangle.

Find the total area covered by all rectangles in the plane.  Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:

    Input: [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
    Output: 6
    Explanation: As illustrated in the picture.

Example 2:

    Input: [[0,0,1000000000,1000000000]]
    Output: 49
    Explanation: The answer is 10^18 modulo (10^9 + 7), which is (10^9)^2 = (-7)^2 = 49.

Note:

- 1 <= rectangles.length <= 200
- rectanges[i].length = 4
- 0 <= rectangles[i][j] <= 10^9
- The total area covered by all rectangles will never exceed 2^63 - 1 and thus will fit in a 64-bit signed integer.

## Method:

try to use stack to calculate the area, but wrong idea due to mutiple overlay:

    class Solution(object):
        def rectangleArea(self, rectangles):
            """
            :type rectangles: List[List[int]]
            :rtype: int
            """
            MOD=10**9 + 7
            rectangles.sort(key=lambda i: i[0])
            rectangles.append([10**9,0,10**9+1,0])
            stack=[]
            area=0
            for r in rectangles:
                if not stack or r[0]<stack[-1][2]:
                    if not stack or r[2]>stack[-1][2]:
                        stack.append(r)
                    else:
                        area+=((r[2]-r[0])*max(0, r[3]-stack[-1][3]))%MOD
                else:
                    while stack:
                        last=stack.pop()
                        area+=((last[2]-last[0])*(last[3]-last[1]))%MOD
                        if not stack:
                            stack.append(r)
                            break
                        if stack[-1][3]<last[3]:
                            area-=(stack[-1][2]-last[0])*(last[3]-last[1])
                        else:
                            area-=(stack[-1][2]-last[0])*(stack[-1][3]-last[1])
            return area%MOD
            
## Solution:

sort and use index to mark the value, loop the area, mark the visited and finally calculate:

O(n^3)

    class Solution(object):
        def rectangleArea(self, rectangles):
            """
            :type rectangles: List[List[int]]
            :rtype: int
            """
            xlist=sorted(list(set(x for x1, y1, x2, y2 in rectangles for x in (x1, x2))))
            ylist=sorted(list(set(y for x1, y1, x2, y2 in rectangles for y in (y1, y2))))
            dx={v:i for i, v in enumerate(xlist)}
            dy={v:i for i, v in enumerate(ylist)}
            dp=[[False]*len(ylist) for _ in range(len(xlist))]
            for x1, y1, x2, y2 in rectangles:
                for x in range(dx[x1], dx[x2]):
                    for y in range(dy[y1], dy[y2]):
                        dp[x][y]=True
            area=0
            for i in range(len(xlist)-1):
                for j in range(len(ylist)-1):
                    if dp[i][j]:
                        area=(area+(xlist[i+1]-xlist[i])*(ylist[j+1]-ylist[j]))%(10**9+7)
            return area
            
line sweep, keep track of the area in each line x using `cnt` and index:

O(n^2):

    class Solution(object):
        def rectangleArea(self, rectangles):
            """
            :type rectangles: List[List[int]]
            :rtype: int
            """
            ylist=sorted(list(set(y for x1, y1, x2, y2 in rectangles for y in (y1, y2))))
            dy={v:i for i, v in enumerate(ylist)}
            cnt=[0]*len(ylist)
            res=[]
            for x1, y1, x2, y2 in rectangles:
                res.append([x1, y1, y2, 1])
                res.append([x2, y1, y2, -1])
            res.sort()
            prev=None
            area=0
            for x, y1, y2, sig in res:
                if prev is not None:
                    s=0
                    for i in range(len(cnt)-1):
                        if cnt[i]:
                            s+=ylist[i+1]-ylist[i]
                    area+=s*(x-prev)
                    area%=10**9+7
                for i in range(dy[y1], dy[y2]):
                    cnt[i]+=sig
                prev=x
            return area