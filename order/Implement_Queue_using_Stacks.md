# 232. Implement Queue using Stacks

Implement the following operations of a queue using stacks.

    push(x) -- Push element x to the back of queue.
    pop() -- Removes the element from in front of queue.
    peek() -- Get the front element.
    empty() -- Return whether the queue is empty.

Notes:
- You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
- Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
- You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

## Method:

two stacks, push O(1), top O(1), pop O(n):

    class MyQueue(object):
    
        def __init__(self):
            """
            Initialize your data structure here.
            """
            self.stack1=[]
            self.stack2=[]
            
        def push(self, x):
            """
            Push element x to the back of queue.
            :type x: int
            :rtype: void
            """
            if not self.stack1:
                self.t=x
            self.stack1.append(x)
    
        def pop(self):
            """
            Removes the element from in front of queue and returns that element.
            :rtype: int
            """
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            res=self.stack2.pop()
            if self.stack2:
                self.t=self.stack2[-1]
            while self.stack2:
                self.stack1.append(self.stack2.pop())
            return res
    
        def peek(self):
            """
            Get the front element.
            :rtype: int
            """
            return self.t
    
        def empty(self):
            """
            Returns whether the queue is empty.
            :rtype: bool
            """
            return len(self.stack1)==0
    
    
    # Your MyQueue object will be instantiated and called as such:
    # obj = MyQueue()
    # obj.push(x)
    # param_2 = obj.pop()
    # param_3 = obj.peek()
    # param_4 = obj.empty()
    
two stacks, push O(n), top O(1), pop O(1):
    
    class MyQueue(object):
    
        def __init__(self):
            """
            Initialize your data structure here.
            """
            self.stack1=[]
            self.stack2=[]
            
        def push(self, x):
            """
            Push element x to the back of queue.
            :type x: int
            :rtype: void
            """
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            self.stack1.append(x)
            while self.stack2:
                self.stack1.append(self.stack2.pop())
    
        def pop(self):
            """
            Removes the element from in front of queue and returns that element.
            :rtype: int
            """
            return self.stack1.pop()
    
        def peek(self):
            """
            Get the front element.
            :rtype: int
            """
            return self.stack1[-1]
    
        def empty(self):
            """
            Returns whether the queue is empty.
            :rtype: bool
            """
            return len(self.stack1)==0
    
    
    # Your MyQueue object will be instantiated and called as such:
    # obj = MyQueue()
    # obj.push(x)
    # param_2 = obj.pop()
    # param_3 = obj.peek()
    # param_4 = obj.empty()
    
## Solution:

two stacks, push O(1), top O(1), pop amortized O(1):
    
    class MyQueue(object):
    
        def __init__(self):
            """
            Initialize your data structure here.
            """
            self.stack1=[]
            self.stack2=[]
            
        def push(self, x):
            """
            Push element x to the back of queue.
            :type x: int
            :rtype: void
            """
            if not self.stack1:
                self.t=x
            self.stack1.append(x)
    
        def pop(self):
            """
            Removes the element from in front of queue and returns that element.
            :rtype: int
            """
            if not self.stack2:
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
    
        def peek(self):
            """
            Get the front element.
            :rtype: int
            """
            return self.stack2[-1] if self.stack2 else self.t
    
        def empty(self):
            """
            Returns whether the queue is empty.
            :rtype: bool
            """
            return len(self.stack1)==0 and len(self.stack2)==0
    
    
    # Your MyQueue object will be instantiated and called as such:
    # obj = MyQueue()
    # obj.push(x)
    # param_2 = obj.pop()
    # param_3 = obj.peek()
    # param_4 = obj.empty()