# 141. Linked List Cycle

Given a linked list, determine if it has a cycle in it.

Follow up:
- Can you solve it without using extra space?

## Method:

Using set as extra space:

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def hasCycle(self, head):
            """
            :type head: ListNode
            :rtype: bool
            """
            s=set()
            while head:
                if head not in s:
                    s.add(head)
                    head=head.next
                else:
                    return True
            return False
            
No extra space, two pointers:

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def hasCycle(self, head):
            """
            :type head: ListNode
            :rtype: bool
            """
            fast=slow=head
            while fast and fast.next:
                fast=fast.next.next
                slow=slow.next
                if fast==slow:
                    return True
            return False