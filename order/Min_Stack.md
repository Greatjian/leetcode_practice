# 155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

- push(x) -- Push element x onto stack.
- pop() -- Removes the element on top of the stack.
- top() -- Get the top element.
- getMin() -- Retrieve the minimum element in the stack.

Example:

    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin();   --> Returns -3.
    minStack.pop();
    minStack.top();      --> Returns 0.
    minStack.getMin();   --> Returns -2.
    
## Method:

因为最小数可能被pop出，所以append需要额外存储次小数：

    class MinStack(object):
    
        def __init__(self):
            """
            initialize your data structure here.
            """
            self.stack=[]
    
        def push(self, x):
            """
            :type x: int
            :rtype: void
            """
            curMin=self.getMin()
            if curMin==None or curMin>x:
                curMin=x
            self.stack.append((x, curMin))   
    
        def pop(self):
            """
            :rtype: void
            """
            self.stack.pop()
    
        def top(self):
            """
            :rtype: int
            """
            return self.stack[-1][0]
    
        def getMin(self):
            """
            :rtype: int
            """
            if not self.stack:
                return None
            return self.stack[-1][1]
    
    # Your MinStack object will be instantiated and called as such:
    # obj = MinStack()
    # obj.push(x)
    # obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.getMin()