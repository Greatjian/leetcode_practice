# 024. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

For example,
    
    Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

## Method:

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def swapPairs(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            dummy=ListNode(0)
            dummy.next=head
            h=dummy
            if not dummy.next:
                return h.next
            while dummy.next.next:
                n=dummy.next.next
                dummy.next.next=dummy.next.next.next
                n.next=dummy.next
                dummy.next=n
                dummy=dummy.next.next
                if not dummy.next:
                    return h.next
            return h.next
            
## Solution:

shorter:

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def swapPairs(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            dummy=ListNode(0)
            dummy.next=head
            h=dummy
            while dummy.next and dummy.next.next:
                n=dummy.next.next
                dummy.next.next=dummy.next.next.next
                n.next=dummy.next
                dummy.next=n
                dummy=dummy.next.next
            return h.next