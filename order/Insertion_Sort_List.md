# 147. Insertion Sort List

Sort a linked list using insertion sort.

## Method:

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def insertionSortList(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            dummy = ListNode(0)
            pre=dummy
            cur=head
            while cur:
                while pre.next and pre.next.val<cur.val:
                    pre=pre.next
                next=cur.next
                cur.next=pre.next
                pre.next=cur
                pre=dummy
                cur=next
            return dummy.next