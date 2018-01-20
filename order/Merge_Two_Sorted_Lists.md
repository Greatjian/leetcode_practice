# 021. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4
    
## Method:

or:

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def mergeTwoLists(self, l1, l2):
            """
            :type l1: ListNode
            :type l2: ListNode
            :rtype: ListNode
            """
            n=ListNode(0)
            head=n
            while l1 or l2:
                if l1:
                    v1=l1.val
                else:
                    v1=float('inf')
                if l2:
                    v2=l2.val
                else:
                    v2=float('inf')
                if v1<v2:
                    n.next=ListNode(v1)
                    n=n.next
                    l1=l1.next
                else:
                    n.next=ListNode(v2)
                    n=n.next
                    l2=l2.next
            return head.next
            
and:

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def mergeTwoLists(self, l1, l2):
            """
            :type l1: ListNode
            :type l2: ListNode
            :rtype: ListNode
            """
            n=ListNode(0)
            head=n
            while l1 and l2:
                if l1.val<l2.val:
                    n.next=ListNode(l1.val)
                    n=n.next
                    l1=l1.next
                else:
                    n.next=ListNode(l2.val)
                    n=n.next
                    l2=l2.next
            if l1:
                n.next=l1
            else:
                n.next=l2
            return head.next