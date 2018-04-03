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