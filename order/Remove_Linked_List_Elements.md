# 203. Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

    Example
    Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
    Return: 1 --> 2 --> 3 --> 4 --> 5

## Method:

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def removeElements(self, head, val):
            """
            :type head: ListNode
            :type val: int
            :rtype: ListNode
            """
            dummy=ListNode(0)
            h, prev=head, dummy
            dummy.next=head
            while h:
                while h and h.val!=val:
                    prev=h
                    h=h.next
                while h and h.val==val:
                    h=h.next
                prev.next=h
            return dummy.next
            
或者：

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def removeElements(self, head, val):
            """
            :type head: ListNode
            :type val: int
            :rtype: ListNode
            """
            dummy=ListNode(0)
            dummy.next=head
            cur, prev=head, dummy
            while cur:
                if cur.val==val:
                    cur=cur.next
                    prev.next=cur
                else:
                    cur=cur.next
                    prev=prev.next
            return dummy.next