# 083. Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,

    Given 1->1->2, return 1->2.
    Given 1->1->2->3->3, return 1->2->3.
    
## Method:

similar as previous one:

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
            pre=dummy
            dummy.next=head
            while head and head.next:
                if head.next.val==head.val:
                    while head.next and head.next.val==head.val:
                        head=head.next
                    pre.next=head
                else:
                    head=head.next
                    pre=pre.next
            return dummy.next
            
using extra space:

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
            h=dummy
            l=[]
            while head:
                if head.val not in l:
                    l.append(head.val)
                head=head.next
            for k in l:
                dummy.next=ListNode(k)
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
            cur=head
            while cur and cur.next:
                if cur.next.val==cur.val:
                    cur.next=cur.next.next
                else:
                    cur=cur.next
            return head