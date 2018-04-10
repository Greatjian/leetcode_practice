# 812. Largest Triangle Area

You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:

    Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
    Output: 2
    Explanation: 
    The five points are show in the figure below. The red triangle is the largest.
    
## Method:

余弦定理：

    class Solution(object):
        def largestTriangleArea(self, points):
            """
            :type points: List[List[int]]
            :rtype: float
            """
            res=float('-inf')
            for i in range(len(points)):
                for j in range(i+1, len(points)):
                    for k in range(j+1, len(points)):
                        res=max(res, self.getArea(points[i], points[j], points[k]))
            return res
            
        def getArea(self, a, b, c):
            l1=((a[1]-b[1])**2+(a[0]-b[0])**2)**0.5
            l2=((a[1]-c[1])**2+(a[0]-c[0])**2)**0.5
            l3=((c[1]-b[1])**2+(c[0]-b[0])**2)**0.5
            cos=(l1**2+l2**2-l3**2)/(2*l1*l2)
            if cos**2>1:
                return 0
            sin=(1-cos**2)**0.5
            return 0.5*l1*l2*sin
            
Helen Equation:

    class Solution:
        def largestTriangleArea(self, points):
            """
            :type points: List[List[int]]
            :rtype: float
            """
            max_area = 0
            for i in range(len(points)-2):
                for j in range(i+1, len(points)-1):
                    for k in range(j+1, len(points)):
                        max_area = max(max_area, self.area(points[i], points[j], points[k]))
            return max_area
                        
        def area(self, a, b, c):
            a1 = ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
            b1 = ((c[0]-b[0])**2+(c[1]-b[1])**2)**0.5
            c1 = ((a[0]-c[0])**2+(a[1]-c[1])**2)**0.5
            p = (a1+b1+c1)/2
            area = (p*abs(p-a1)*abs(p-b1)*abs(p-c1))**0.5
            return area