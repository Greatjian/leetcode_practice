# 092. Reverse Linked List II

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:

    Given 1->2->3->4->5->NULL, m = 2 and n = 4,
    
    return 1->4->3->2->5->NULL.

Note:
- Given m, n satisfy the following condition:
- 1 ≤ m ≤ n ≤ length of list.

## Method:

multiple pointers:

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def reverseBetween(self, head, m, n):
            """
            :type head: ListNode
            :type m: int
            :type n: int
            :rtype: ListNode
            """
            dummy=ListNode(0)
            front=dummy
            dummy.next=head
            for i in range(m-1):
                front=front.next
                head=head.next
            prev=front.next
            head=head.next
            for i in range(n-m):
                cur=head
                head=head.next
                cur.next=prev
                prev=cur
            front.next.next=head
            front.next=prev
            return dummy.next