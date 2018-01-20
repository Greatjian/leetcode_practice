# 061. Rotate List

Given a list, rotate the list to the right by k places, where k is non-negative.

    Example:

    Given 1->2->3->4->5->NULL and k = 2,
    
    return 4->5->1->2->3->NULL.

## Method:

Using three pointers:

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def rotateRight(self, head, k):
            """
            :type head: ListNode
            :type k: int
            :rtype: ListNode
            """
            if not head:
                return head
            c=1
            first, second, h=head, head, head
            while h.next:
                h=h.next
                c+=1
            h.next=head
            for i in range(k%c):
                first=first.next
            while first!=h:
                first=first.next
                second=second.next
            res=second.next
            second.next=None
            return res
            
## Solution:

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def rotateRight(self, head, k):
            """
            :type head: ListNode
            :type k: int
            :rtype: ListNode
            """
            if not head:
                return head
            count=1
            first=head
            while first.next:
                first=first.next
                count+=1
            first.next=head
            for i in range(count-k%count):
                first=first.next
            res=first.next
            first.next=None
            return res