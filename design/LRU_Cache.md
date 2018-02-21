# 146. LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

    get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.

    put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
- Could you do both operations in O(1) time complexity?

Example:

    LRUCache cache = new LRUCache( 2 /* capacity */ );
    
    cache.put(1, 1);
    cache.put(2, 2);
    cache.get(1);       // returns 1
    cache.put(3, 3);    // evicts key 2
    cache.get(2);       // returns -1 (not found)
    cache.put(4, 4);    // evicts key 1
    cache.get(1);       // returns -1 (not found)
    cache.get(3);       // returns 3
    cache.get(4);       // returns 4
    
## Method:

queue + dict, both O(n) when it shows up in the dict, tle:

    class LRUCache(object):
    
        def __init__(self, capacity):
            """
            :type capacity: int
            """
            self.l=capacity
            self.queue=collections.deque()
            self.d={}
            
    
        def get(self, key):
            """
            :type key: int
            :rtype: int
            """
            if key not in self.d:
                return -1
            for _ in range(len(self.queue)):
                if self.queue[0]!=key:
                    self.queue.append(self.queue.popleft())
                else:
                    self.queue.popleft()
            self.queue.append(key)
            return self.d[key]
            
    
        def put(self, key, value):
            """
            :type key: int
            :type value: int
            :rtype: void
            """
            if key not in self.d:
                self.d[key]=value
                self.queue.append(key)
                if len(self.queue)>self.l:
                    del self.d[self.queue.popleft()]
            else:
                for _ in range(len(self.queue)):
                    if self.queue[0]!=key:
                        self.queue.append(self.queue.popleft())
                    else:
                        self.queue.popleft()
                self.queue.append(key)
                self.d[key]=value
    
    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)
    
## Solution:

doubly linked list + dict:

    class Node(object):
        def __init__(self, key, value):
            self.key=key
            self.value=value
            self.prev=None
            self.next=None
    
    class LRUCache(object):
        def __init__(self, capacity):
            """
            :type capacity: int
            """
            self.l=capacity
            self.head=Node(0, 0)
            self.tail=Node(0, 0)
            self.head.next=self.tail
            self.tail.prev=self.head
            self.d={}
            
    
        def get(self, key):
            """
            :type key: int
            :rtype: int
            """
            if key not in self.d:
                return -1
            node=self.d[key]
            self._remove(node)
            self._add(node)
            return self.d[key].value
            
    
        def put(self, key, value):
            """
            :type key: int
            :type value: int
            :rtype: void
            """
            if key not in self.d:
                node=Node(key, value)
                self.d[key]=node
                self._add(node)
                if len(self.d)>self.l:
                    node=self.head.next
                    self._remove(node)
                    del self.d[node.key]
            else:
                node=self.d[key]
                self._remove(node)
                self._add(node)
                self.d[key].value=value
                
        def _remove(self, node):
            p=node.prev
            n=node.next
            p.next=n
            n.prev=p
    
        def _add(self, node):
            p=self.tail.prev
            p.next=node
            node.prev=p
            node.next=self.tail
            self.tail.prev=node
    
    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)