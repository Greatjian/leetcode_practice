# 042. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 

    Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
    
## Method:

two pointers:

    class Solution(object):
        def trap(self, height):
            """
            :type height: List[int]
            :rtype: int
            """
            left, right=0, len(height)-1
            area=0
            maxLeft, maxRight=0, 0
            while left<right:
                maxLeft=max(maxLeft, height[left])
                maxRight=max(maxRight, height[right])
                if maxLeft<maxRight:
                    area+=maxLeft-height[left]
                    left+=1
                else:
                    area+=maxRight-height[right]
                    right-=1
            return area
            
dp (easier to understand):

    class Solution(object):
        def trap(self, height):
            """
            :type height: List[int]
            :rtype: int
            """
            l=len(height)
            maxLeft=maxRight=float('-inf')
            left, right=[0]*l, [0]*l
            for i in range(l):
                if height[i]>maxLeft:
                    maxLeft=height[i]
                left[i]=maxLeft
            for i in range(l-1, -1, -1):
                if height[i]>maxRight:
                    maxRight=height[i]
                right[i]=maxRight
            return sum(min(left[i], right[i])-height[i] for i in range(l))