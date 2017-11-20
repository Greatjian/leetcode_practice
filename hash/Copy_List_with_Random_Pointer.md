# 138. Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

## Solution:

defaultdict():

    # Definition for singly-linked list with a random pointer.
    # class RandomListNode(object):
    #     def __init__(self, x):
    #         self.label = x
    #         self.next = None
    #         self.random = None
    
    class Solution(object):
        def copyRandomList(self, head):
            """
            :type head: RandomListNode
            :rtype: RandomListNode
            """
            dic = collections.defaultdict(lambda: RandomListNode(0))
            dic[None] = None
            n = head
            while n:
                dic[n].label = n.label
                dic[n].next = dic[n.next]
                dic[n].random = dic[n.random]
                n = n.next
            return dic[head]
            
dict()(need to iterate twice):

    # Definition for singly-linked list with a random pointer.
    # class RandomListNode(object):
    #     def __init__(self, x):
    #         self.label = x
    #         self.next = None
    #         self.random = None
    
    class Solution(object):
        def copyRandomList(self, head):
            """
            :type head: RandomListNode
            :rtype: RandomListNode
            """
            p1 = head
            old_new = {None: None}
            while p1:
                old_new[p1] = RandomListNode(p1.label)
                p1 = p1.next
            p1 = head
            while p1:
                old_new[p1].next = old_new[p1.next]
                old_new[p1].random = old_new[p1.random]
                p1 = p1.next
            return old_new[head]