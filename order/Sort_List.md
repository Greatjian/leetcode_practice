# 148. Sort List

Sort a linked list in O(n log n) time using constant space complexity.

## Method:

mergesort:

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def sortList(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            if not head or not head.next:
                return head
            fast, slow=head, head
            while fast and fast.next:
                fast=fast.next.next
                prev=slow
                slow=slow.next
            prev.next=None
            left=self.sortList(head)
            right=self.sortList(slow)
            return self.merge(left, right)
        
        def merge(self, l, r):
            dummy=ListNode(0)
            cur=dummy
            while l and r:
                if l.val<r.val:
                    cur.next=l
                    l=l.next
                else:
                    cur.next=r
                    r=r.next
                cur=cur.next
            if not l:
                cur.next=r
            else:
                cur.next=l
            return dummy.next