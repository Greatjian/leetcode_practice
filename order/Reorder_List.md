# 143. Reorder List

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,

    Given {1,2,3,4}, reorder it to {1,4,2,3}.

## Method:

recursion, O(nlogn), tle:

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def reorderList(self, head):
            """
            :type head: ListNode
            :rtype: void Do not return anything, modify head in-place instead.
            """
            if not head or not head.next:
                return
            tail=head
            while tail.next:
                t=tail
                tail=tail.next
            if t!=head:
                tail.next=head.next
                head.next=tail
                t.next=None
            return self.reorderList(tail.next)
            
## Solution:

O(n),

- Find the middle of the list

> 1->2->3->4->5->6

- Reverse the half after middle

> 1->2->3->4<-5<-6
         |
        null

- Start reorder one by one

> 1->6->2->5->3->4


    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def reorderList(self, head):
            """
            :type head: ListNode
            :rtype: void Do not return anything, modify head in-place instead.
            """
            fast, slow=head, head
            while fast and fast.next:
                fast=fast.next.next
                slow=slow.next
                
            prev=None
            while slow:
                next=slow.next
                slow.next=prev
                prev=slow
                slow=next
            
            begin=head
            while begin:
                nbegin=begin.next
                begin.next=prev
                begin=begin.next
                prev=nbegin