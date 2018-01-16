# 593. Valid Square

Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:

    Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
    Output: True

Note:

- All the input integers are in the range [-10000, 10000].
- A valid square has four equal sides with positive length and four equal angles (90-degree angles).
- Input points have no order.

## Method:

compute distance:

    class Solution(object):
        def validSquare(self, p1, p2, p3, p4):
            """
            :type p1: List[int]
            :type p2: List[int]
            :type p3: List[int]
            :type p4: List[int]
            :rtype: bool
            """
            d=collections.defaultdict(int)
            for p in [p1, p2, p3, p4]:
                for q in [p1, p2, p3, p4]:
                    if p!=q:
                        d[self.computeDistanceSquare(p, q)]+=1
            res=[]
            for k in d.keys():
                res.append(k)
                res.append(d[k])
            if len(res)!=4:
                return False
            if res[0]*2==res[2] and res[1]==8 and res[3]==4 or res[2]*2==res[0] and res[3]==8 and res[1]==4:
                return True
            return False
            
        def computeDistanceSquare(self, p, q):
            return (p[0]-q[0])**2+(p[1]-q[1])**2
            
check easier:

    class Solution(object):
        def validSquare(self, p1, p2, p3, p4):
            """
            :type p1: List[int]
            :type p2: List[int]
            :type p3: List[int]
            :type p4: List[int]
            :rtype: bool
            """
            s=set()
            s.add(self.computeDistanceSquare(p1, p2))
            s.add(self.computeDistanceSquare(p1, p3))
            s.add(self.computeDistanceSquare(p1, p4))
            s.add(self.computeDistanceSquare(p2, p3))
            s.add(self.computeDistanceSquare(p2, p4))
            s.add(self.computeDistanceSquare(p3, p4))
            return len(s)==2 and 0 not in s
            
        def computeDistanceSquare(self, p, q):
            return (p[0]-q[0])**2+(p[1]-q[1])**2