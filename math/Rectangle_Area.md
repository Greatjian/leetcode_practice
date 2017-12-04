# 223. Rectangle Area

Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area

Assume that the total area is never beyond the maximum possible value of int.

## Method;

分类讨论：

    class Solution(object):
        def computeArea(self, A, B, C, D, E, F, G, H):
            """
            :type A: int
            :type B: int
            :type C: int
            :type D: int
            :type E: int
            :type F: int
            :type G: int
            :type H: int
            :rtype: int
            """
            inter=min(C-A, G-E, abs(G-A), abs(C-E))*min(D-B, H-F, abs(H-B), abs(D-F))
            if min(A, C)>max(E, G) or min(E, G)>max(A, C) or min(B, D)>max(F, H) or min(F, H)>max(B, D):
                inter=0
            return (C-A)*(D-B)+(G-E)*(H-F)-inter
            
## Solution:

shorter version:

    class Solution(object):
        def computeArea(self, A, B, C, D, E, F, G, H):
            """
            :type A: int
            :type B: int
            :type C: int
            :type D: int
            :type E: int
            :type F: int
            :type G: int
            :type H: int
            :rtype: int
            """
            inter=(min(C, G)-max(A, E))*(min(D, H)- max(B, F))
            if min(A, C)>max(E, G) or min(E, G)>max(A, C) or min(B, D)>max(F, H) or min(F, H)>max(B, D):
                inter=0
            return (C-A)*(D-B)+(G-E)*(H-F)-inter