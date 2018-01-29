# 225. Implement Stack using Queues

Implement the following operations of a stack using queues.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    empty() -- Return whether the stack is empty.

Notes:
- You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
- Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
- You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

## Method:

two queues, pop O(n), top O(n), push O(1):

    class MyStack(object):
    
        def __init__(self):
            """
            Initialize your data structure here.
            """
            self.queue1=collections.deque([])
            self.queue2=collections.deque([])
    
        def push(self, x):
            """
            Push element x onto stack.
            :type x: int
            :rtype: void
            """
            self.queue1.append(x)
            
    
        def pop(self):
            """
            Removes the element on top of the stack and returns that element.
            :rtype: int
            """
            while len(self.queue1)>1:
                self.queue2.append(self.queue1.popleft())
            res=self.queue1.popleft()
            while self.queue2:
                self.queue1.append(self.queue2.popleft())
            return res
    
        def top(self):
            """
            Get the top element.
            :rtype: int
            """
            while len(self.queue1)>1:
                self.queue2.append(self.queue1.popleft())
            res=self.queue1.popleft()
            self.queue2.append(res)
            while self.queue2:
                self.queue1.append(self.queue2.popleft())
            return res
    
        def empty(self):
            """
            Returns whether the stack is empty.
            :rtype: bool
            """
            return len(self.queue1)==0
            
    
    
    # Your MyStack object will be instantiated and called as such:
    # obj = MyStack()
    # obj.push(x)
    # param_2 = obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.empty()
    
## Solution:

keep track of a variable t can make top O(1)

two queues, pop O(n), top O(1), push O(1):

    class MyStack(object):
    
        def __init__(self):
            """
            Initialize your data structure here.
            """
            self.queue1=collections.deque([])
            self.queue2=collections.deque([])
    
        def push(self, x):
            """
            Push element x onto stack.
            :type x: int
            :rtype: void
            """
            self.queue1.append(x)
            self.t=x
            
    
        def pop(self):
            """
            Removes the element on top of the stack and returns that element.
            :rtype: int
            """
            while len(self.queue1)>1:
                self.queue2.append(self.queue1.popleft())
            res=self.queue1.popleft()
            while self.queue2:
                self.queue1.append(self.queue2.popleft())
            if len(self.queue1)!=0:
                self.t=self.queue1[-1]
            return res
    
        def top(self):
            """
            Get the top element.
            :rtype: int
            """
            return self.t
    
        def empty(self):
            """
            Returns whether the stack is empty.
            :rtype: bool
            """
            return len(self.queue1)==0
            
    
    
    # Your MyStack object will be instantiated and called as such:
    # obj = MyStack()
    # obj.push(x)
    # param_2 = obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.empty()
    
one queue, pop O(1), top O(1), push O(n):

    class MyStack(object):
    
        def __init__(self):
            """
            Initialize your data structure here.
            """
            self.queue=collections.deque([])
    
        def push(self, x):
            """
            Push element x onto stack.
            :type x: int
            :rtype: void
            """
            self.queue.append(x)
            for _ in range(x-1):
                self.queue.append(self.queue.popleft())
            
    
        def pop(self):
            """
            Removes the element on top of the stack and returns that element.
            :rtype: int
            """
            return self.queue.popleft()
    
        def top(self):
            """
            Get the top element.
            :rtype: int
            """
            return self.queue[0]
    
        def empty(self):
            """
            Returns whether the stack is empty.
            :rtype: bool
            """
            return len(self.queue)==0
            
    
    
    # Your MyStack object will be instantiated and called as such:
    # obj = MyStack()
    # obj.push(x)
    # param_2 = obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.empty()