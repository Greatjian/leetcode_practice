# 082. Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,

    Given 1->2->3->3->4->4->5, return 1->2->5.
    Given 1->1->1->2->3, return 2->3.
    
## Method:

ordereddict:

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def deleteDuplicates(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            d=collections.OrderedDict()
            while head:
                if head.val not in d:
                    d[head.val]=1
                else:
                    d[head.val]+=1
                head=head.next
            dummy=ListNode(0)
            h=dummy
            for v in d.keys():
                if d[v]==1:
                    dummy.next=ListNode(v)
                    dummy=dummy.next
            return h.next
            
## Solution:

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def deleteDuplicates(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            dummy=ListNode(0)
            dummy.next=head
            pre=dummy
            while head and head.next:
                if head.val==head.next.val:
                    while head.next and head.val==head.next.val:
                        head=head.next
                    head=head.next
                    pre.next=head
                else:
                    head=head.next
                    pre=pre.next
            return dummy.next