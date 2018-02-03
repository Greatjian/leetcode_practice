# 251. Flatten 2D Vector

Implement an iterator to flatten a 2d vector.

    For example,
    Given 2d vector =
    
    [
      [1,2],
      [3],
      [4,5,6]
    ]

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].

Follow up:
- As an added challenge, try to code it using only iterators in C++ or iterators in Java.

## Method:

    class Vector2D(object):
    
        def __init__(self, vec2d):
            """
            Initialize your data structure here.
            :type vec2d: List[List[int]]
            """
            self.list=[]
            for i in range(len(vec2d)-1, -1, -1):
                for j in range(len(vec2d[i])-1, -1, -1):
                    self.list.append(vec2d[i][j])
            
        def next(self):
            """
            :rtype: int
            """
            return self.list.pop()
    
        def hasNext(self):
            """
            :rtype: bool
            """
            return self.list
    
    # Your Vector2D object will be instantiated and called as such:
    # i, v = Vector2D(vec2d), []
    # while i.hasNext(): v.append(i.next())
    
## Solution:

i, j pointer, O(1) space:

    class Vector2D(object):
    
        def __init__(self, vec2d):
            """
            Initialize your data structure here.
            :type vec2d: List[List[int]]
            """
            self.i, self.j=0, 0
            self.vec=vec2d
            
        def next(self):
            """
            :rtype: int
            """
            self.j+=1
            return self.vec[self.i][self.j-1]
    
        def hasNext(self):
            """
            :rtype: bool
            """
            if not self.vec:
                return False
            if self.j==len(self.vec[self.i]):
                self.j=0
                self.i+=1
                while self.i<len(self.vec) and not self.vec[self.i]:
                    self.i+=1
            return self.i!=len(self.vec)
    
    # Your Vector2D object will be instantiated and called as such:
    # i, v = Vector2D(vec2d), []
    # while i.hasNext(): v.append(i.next())
    
self.hasNext:

        def hasNext(self):
            """
            :rtype: bool
            """
            while self.i<len(self.vec):
                if self.j<len(self.vec[self.i]):
                    return True
                self.j=0
                self.i+=1
            return False