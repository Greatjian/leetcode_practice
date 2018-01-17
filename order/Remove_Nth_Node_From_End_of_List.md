# 019. Remove Nth Node From End of List

Given a linked list, remove the nth node from the end of list and return its head.

For example,

    Given linked list: 1->2->3->4->5, and n = 2.
    After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
- Given n will always be valid.
- Try to do this in one pass.

## Method:

one pointer, two passes:

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def removeNthFromEnd(self, head, n):
            """
            :type head: ListNode
            :type n: int
            :rtype: ListNode
            """
            h1, h2=head, head
            l=1
            while head.next:
                head=head.next
                l+=1
            if l-n==0:
                return h2.next
            for i in range(l-n-1):
                h1=h1.next
            h1.next=h1.next.next
            return h2 
            
Using dummy node, save one check (l-n=0):

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def removeNthFromEnd(self, head, n):
            """
            :type head: ListNode
            :type n: int
            :rtype: ListNode
            """
            dummy=ListNode(0)
            dummy.next=head
            first=dummy
            l=1
            while head:
                head=head.next
                l+=1
            for i in range(l-n-1):
                first=first.next
            first.next=first.next.next
            return dummy.next
            
## Solution:

two pointers, one pass:

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def removeNthFromEnd(self, head, n):
            """
            :type head: ListNode
            :type n: int
            :rtype: ListNode
            """
            dummy=ListNode(0)
            dummy.next=head
            first, second=dummy, dummy
            for i in range(n):
                first=first.next
            while first.next:
                first=first.next
                second=second.next
            second.next=second.next.next
            return dummy.next