# 011. Container With Most Water

Given n non-negative integers a1, a2, ..., an, 
where each represents a point at coordinate (i, ai). 

n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, 
such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

## Method:

default value: two lines at each end. 
Moving the smaller one to the center at each step while checking the total area.

time complexity: O(n)

first try:
```
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height[0]>height[-1]:
            height=height[::-1]
        area=height[0]*(len(height)-1)
        for i in range(len(height)):
            if height[i+1]*(len(height)-2-i)>area:
                area=height[i+1]*(len(height)-1-i)
```
second try:
```
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1          #NOT right=-1!
        area=min(height[left],height[right])*(len(height)-1)
        while (left<right):
            if height[left]<height[right]:
                left+=1
                if min(height[left],height[right])*(right-left)>area:
                    area=min(height[left],height[right])*(right-left)
            else:
                right-=1
                if min(height[left],height[right])*(right-left)>area:
                    area=min(height[left],height[right])*(right-left)
        return area
```
submission accepted!

## Solution

    class Solution(object):
        def maxArea(self, height):
            """
            :type height: List[int]
            :rtype: int
            """
            left, right=0, len(height)-1
            area=float('-inf')
            while left<right:
                area=max(area, min(height[left],height[right])*(right-left))
                if height[left]<height[right]:
                    left+=1
                else:
                    right-=1
            return area

