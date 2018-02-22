# 295. Find Median from Data Stream

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples: 

    [2,3,4] , the median is 3
    
    [2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

- void addNum(int num) - Add a integer number from the data stream to the data structure.
- double findMedian() - Return the median of all elements so far.

For example:

    addNum(1)
    addNum(2)
    findMedian() -> 1.5
    addNum(3) 
    findMedian() -> 2
    
## Method:

list and sort, tle:

    class MedianFinder(object):
    
        def __init__(self):
            """
            initialize your data structure here.
            """
            self.l=[]
    
        def addNum(self, num):
            """
            :type num: int
            :rtype: void
            """
            # O(n)
            i=0
            while i<len(self.l):
                if self.l[i]>num:
                    break
                i+=1
            self.l.insert(i, num)
            
            # O(nlogn) below
            # self.l.append(num)
            # self.l.sort()
    
        def findMedian(self):
            """
            :rtype: float
            """
            l=len(self.l)
            return (self.l[l/2]+self.l[(l-1)/2])/2.0
    
    
    # Your MedianFinder object will be instantiated and called as such:
    # obj = MedianFinder()
    # obj.addNum(num)
    # param_2 = obj.findMedian()
    
## Solution:

minheap and maxheap, O(logn):

    class MedianFinder(object):
    
        def __init__(self):
            """
            initialize your data structure here.
            """
            self.shp, self.lhp=[], []
            self.count=0
    
        def addNum(self, num):
            """
            :type num: int
            :rtype: void
            """
            if not self.shp or num<=-self.shp[0]:
                heapq.heappush(self.shp, -num)
            else:
                heapq.heappush(self.lhp, num)
            if len(self.shp)-len(self.lhp)>1:
                heapq.heappush(self.lhp, -heapq.heappop(self.shp))
            elif len(self.lhp)>len(self.shp):
                heapq.heappush(self.shp, -heapq.heappop(self.lhp))
    
        def findMedian(self):
            """
            :rtype: float
            """
            return -self.shp[0] if (len(self.shp)+len(self.lhp))%2 else (-self.shp[0]+self.lhp[0])/2.0
    
    
    # Your MedianFinder object will be instantiated and called as such:
    # obj = MedianFinder()
    # obj.addNum(num)
    # param_2 = obj.findMedian()