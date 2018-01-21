# 086. Partition List

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,

    Given 1->4->3->2->5->2 and x = 3,
    return 1->2->2->4->3->5.
    
## Method:

using extra space:

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def partition(self, head, x):
            """
            :type head: ListNode
            :type x: int
            :rtype: ListNode
            """
            s=s0=ListNode(0)
            l=l0=ListNode(0)
            s.next=head
            while head:
                if head.val<x:
                    s.next=ListNode(head.val)
                    s=s.next
                else:
                    l.next=ListNode(head.val)
                    l=l.next
                head=head.next
            s.next=l0.next
            return s0.next
            
## Solution:

little modification, solve in-place:

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def partition(self, head, x):
            """
            :type head: ListNode
            :type x: int
            :rtype: ListNode
            """
            s=s0=ListNode(0)
            l=l0=ListNode(0)
            s.next=head
            while head:
                if head.val<x:
                    s.next=head
                    s=s.next
                else:
                    l.next=head
                    l=l.next
                head=head.next
            s.next=l0.next
            l.next=None
            return s0.next