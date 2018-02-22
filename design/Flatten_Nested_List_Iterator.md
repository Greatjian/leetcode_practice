# 341. Flatten Nested List Iterator

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

    Given the list [[1,1],2,[1,1]],
    
    By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:

    Given the list [1,[4,[6]]],
    
    By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].

## Method:

using stack:

    # """
    # This is the interface that allows for creating nested lists.
    # You should not implement it, or speculate about its implementation
    # """
    #class NestedInteger(object):
    #    def isInteger(self):
    #        """
    #        @return True if this NestedInteger holds a single integer, rather than a nested list.
    #        :rtype bool
    #        """
    #
    #    def getInteger(self):
    #        """
    #        @return the single integer that this NestedInteger holds, if it holds a single integer
    #        Return None if this NestedInteger holds a nested list
    #        :rtype int
    #        """
    #
    #    def getList(self):
    #        """
    #        @return the nested list that this NestedInteger holds, if it holds a nested list
    #        Return None if this NestedInteger holds a single integer
    #        :rtype List[NestedInteger]
    #        """
    
    class NestedIterator(object):
    
        def __init__(self, nestedList):
            """
            Initialize your data structure here.
            :type nestedList: List[NestedInteger]
            """
            self.res=collections.deque()
            stack=nestedList[::-1]
            while stack:
                node=stack.pop()
                if node.isInteger():
                    self.res.append(node.getInteger())
                    continue
                if node.getList()==None:
                    continue
                l=node.getList()
                stack+=l[::-1]
    
        def next(self):
            """
            :rtype: int
            """
            return self.res.popleft()
    
        def hasNext(self):
            """
            :rtype: bool
            """
            return self.res
    
    # Your NestedIterator object will be instantiated and called as such:
    # i, v = NestedIterator(nestedList), []
    # while i.hasNext(): v.append(i.next())
    
just using a stack:

    # """
    # This is the interface that allows for creating nested lists.
    # You should not implement it, or speculate about its implementation
    # """
    #class NestedInteger(object):
    #    def isInteger(self):
    #        """
    #        @return True if this NestedInteger holds a single integer, rather than a nested list.
    #        :rtype bool
    #        """
    #
    #    def getInteger(self):
    #        """
    #        @return the single integer that this NestedInteger holds, if it holds a single integer
    #        Return None if this NestedInteger holds a nested list
    #        :rtype int
    #        """
    #
    #    def getList(self):
    #        """
    #        @return the nested list that this NestedInteger holds, if it holds a nested list
    #        Return None if this NestedInteger holds a single integer
    #        :rtype List[NestedInteger]
    #        """
    
    class NestedIterator(object):
    
        def __init__(self, nestedList):
            """
            Initialize your data structure here.
            :type nestedList: List[NestedInteger]
            """
            self.stack=nestedList[::-1]
    
        def next(self):
            """
            :rtype: int
            """
            return self.stack.pop().getInteger()
    
        def hasNext(self):
            """
            :rtype: bool
            """
            while self.stack and not self.stack[-1].isInteger():
                node=self.stack.pop()
                self.stack+=node.getList()[::-1]
            return self.stack
    
    # Your NestedIterator object will be instantiated and called as such:
    # i, v = NestedIterator(nestedList), []
    # while i.hasNext(): v.append(i.next())