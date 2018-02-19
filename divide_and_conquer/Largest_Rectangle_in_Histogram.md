# 084. Largest Rectangle in Histogram

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

    For example,
    Given heights = [2,1,5,6,2,3],
    return 10.

## Method:

divide and conquer, two pointers, O(nlogn):

    class Solution(object):
        def largestRectangleArea(self, heights):
            """
            :type heights: List[int]
            :rtype: int
            """
            return self.helper(0, len(heights)-1, heights) if heights else 0
            
        def helper(self, lo, hi, heights):
            if lo==hi:
                return heights[lo]
            mid=(lo+hi)/2
            area=self.helper(lo, mid, heights)
            area=max(area, self.helper(mid+1, hi, heights))
            area=max(area, self.a(lo, mid, hi, heights))
            return area
    
                
        def a(self, lo, mid, hi, heights):
            i, j=mid, mid+1
            l=min(heights[mid], heights[mid+1])
            s=2*l
            while i>=lo and j<=hi:
                l=min(l, heights[i], heights[j])
                s=max(s, (j-i+1)*l)
                if i==lo:
                    j+=1
                    continue
                if j==hi:
                    i-=1
                    continue
                if heights[i-1]<heights[j+1]:
                    j+=1
                else:
                    i-=1
            return s
                
## Solution

stack, O(n):

    class Solution(object):
        def largestRectangleArea(self, heights):
            """
            :type heights: List[int]
            :rtype: int
            """
            heights.append(0)
            stack=[]
            mh=0
            for i in range(len(heights)):
                while stack and heights[stack[-1]]>heights[i]:
                    j=stack.pop()
                    area=(i-stack[-1]-1 if stack else i)*heights[j]
                    mh=max(mh, area)
                stack.append(i)
            return mh
            
            
                        