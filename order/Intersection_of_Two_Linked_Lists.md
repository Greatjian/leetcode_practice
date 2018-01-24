# 160. Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

    A:          a1 → a2
                       ↘
                         c1 → c2 → c3
                       ↗            
    B:     b1 → b2 → b3

    begin to intersect at node c1.


Notes:

- If the two linked lists have no intersection at all, return null.
- The linked lists must retain their original structure after the function returns.
- You may assume there are no cycles anywhere in the entire linked structure.
- Your code should preferably run in O(n) time and use only O(1) memory.

## Method:

Two loops, calculate difference of length of paths:

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def getIntersectionNode(self, headA, headB):
            """
            :type head1, head1: ListNode
            :rtype: ListNode
            """
            hA, hB=headA, headB
            lA, lB=0, 0
            while hA and hA.next:
                hA=hA.next
                lA+=1
            while hB and hB.next:
                hB=hB.next
                lB+=1
            if hA!=hB:
                return None
            if lA>lB:
                for i in range(lA-lB):
                    headA=headA.next
            else:
                for i in range(lB-lA):
                    headB=headB.next
            while headA!=headB:
                headA=headA.next
                headB=headB.next
            return headA
            
## Solution:

Absolutely brilliant:

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def getIntersectionNode(self, headA, headB):
            """
            :type head1, head1: ListNode
            :rtype: ListNode
            """
            hA, hB=headA, headB
            while hA!=hB:
                hA=hA.next if hA else headB
                hB=hB.next if hB else headA
            return hA