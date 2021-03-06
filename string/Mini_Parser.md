# 385. Mini Parser

Given a nested list of integers represented as a string, implement a parser to deserialize it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Note: You may assume that the string is well-formed:

- String is non-empty.
- String does not contain white spaces.
- String contains only digits 0-9, [, - ,, ].

Example 1:

    Given s = "324",
    
    You should return a NestedInteger object which contains a single integer 324.

Example 2:

    Given s = "[123,[456,[789]]]",
    
    Return a NestedInteger object containing a nested list with 2 elements:
    
    1. An integer containing value 123.
    2. A nested list containing two elements:
        i.  An integer containing value 456.
        ii. A nested list with one element:
             a. An integer containing value 789.

## Method:

fail to use recursion:

    # """
    # This is the interface that allows for creating nested lists.
    # You should not implement it, or speculate about its implementation
    # """
    #class NestedInteger(object):
    #    def __init__(self, value=None):
    #        """
    #        If value is not specified, initializes an empty list.
    #        Otherwise initializes a single integer equal to value.
    #        """
    #
    #    def isInteger(self):
    #        """
    #        @return True if this NestedInteger holds a single integer, rather than a nested list.
    #        :rtype bool
    #        """
    #
    #    def add(self, elem):
    #        """
    #        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
    #        :rtype void
    #        """
    #
    #    def setInteger(self, value):
    #        """
    #        Set this NestedInteger to hold a single integer equal to value.
    #        :rtype void
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
    
    class Solution(object):
        def deserialize(self, s):
            """
            :type s: str
            :rtype: NestedInteger
            """
            if not s:
                return
            n=NestedInteger()
            num=0
            sign=1
            for i in range(len(s)):
                if s[i]=='-':
                    sign=-1
                if s[i].isdigit():
                    num=num*10+int(s[i])
                    if i==len(s)-1:
                        return sign*num
                else:
                    if s[i]==']' and s[i-1]!='[':
                        break
                    if s[i]==',' and s[i-1]!=']':
                        n.add(sign*num)
                        num=0
                    if s[i]=='[' and i!=0:
                        if s[i+1]==']':
                            n.add([])
                        elif i!=len(s)-1:
                            n.add(self.deserialize(s[i+1:]))
            return n
                
  ## Solution:
  
  using eval(str):
  
    # """
    # This is the interface that allows for creating nested lists.
    # You should not implement it, or speculate about its implementation
    # """
    #class NestedInteger(object):
    #    def __init__(self, value=None):
    #        """
    #        If value is not specified, initializes an empty list.
    #        Otherwise initializes a single integer equal to value.
    #        """
    #
    #    def isInteger(self):
    #        """
    #        @return True if this NestedInteger holds a single integer, rather than a nested list.
    #        :rtype bool
    #        """
    #
    #    def add(self, elem):
    #        """
    #        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
    #        :rtype void
    #        """
    #
    #    def setInteger(self, value):
    #        """
    #        Set this NestedInteger to hold a single integer equal to value.
    #        :rtype void
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
    
    class Solution(object):
        def deserialize(self, s):
            """
            :type s: str
            :rtype: NestedInteger
            """
            def nestedInteger(x):
                if isinstance(x, int):
                    return NestedInteger(x)
                lst = NestedInteger()
                for y in x:
                    lst.add(nestedInteger(y))
                return lst
            return nestedInteger(eval(s))
                
iterative:

    # """
    # This is the interface that allows for creating nested lists.
    # You should not implement it, or speculate about its implementation
    # """
    #class NestedInteger(object):
    #    def __init__(self, value=None):
    #        """
    #        If value is not specified, initializes an empty list.
    #        Otherwise initializes a single integer equal to value.
    #        """
    #
    #    def isInteger(self):
    #        """
    #        @return True if this NestedInteger holds a single integer, rather than a nested list.
    #        :rtype bool
    #        """
    #
    #    def add(self, elem):
    #        """
    #        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
    #        :rtype void
    #        """
    #
    #    def setInteger(self, value):
    #        """
    #        Set this NestedInteger to hold a single integer equal to value.
    #        :rtype void
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
    
    class Solution(object):
        def deserialize(self, s):
            """
            :type s: str
            :rtype: NestedInteger
            """
            stack = []
            sign, num = 1, None
            for c in s:
                if c == '[':
                    stack.append(NestedInteger())
                elif c >= '0' and c <= '9':
                    num = (num or 0)*10 + int(c)
                elif c == '-':
                    sign = -1
                else:
                    if num is not None:
                        stack[-1].add(sign * num)
                        sign, num = 1, None
                    if c == ']':
                        top = stack.pop()
                        if stack:
                            stack[-1].add(top)
                        else:
                            return top
            return NestedInteger(sign * num)
            