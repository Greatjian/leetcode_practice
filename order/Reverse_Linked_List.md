# 206. Reverse Linked List

Reverse a singly linked list.

click to show more hints.

Hint:
- A linked list can be reversed either iteratively or recursively. Could you implement both?

## Method:

iterative:

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def reverseList(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            prev=None
            while head:
                new=head.next
                head.next=prev
                prev=head
                head=new
            return prev
            
recursion:

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def reverseList(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            return self.helper(None, head)
            
        def helper(self, prev, head):
            if not head:
                return prev
            new=head.next
            head.next=prev
            return self.helper(head, new)