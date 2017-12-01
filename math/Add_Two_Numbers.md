# 002. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    
## Method:

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def addTwoNumbers(self, l1, l2):
            """
            :type l1: ListNode
            :type l2: ListNode
            :rtype: ListNode
            """
            carryon=0
            h=l=ListNode(None)
            while l1 and l2:
                l.next=ListNode((l1.val+l2.val+carryon)%10)
                carryon=(l1.val+l2.val+carryon)/10
                l1=l1.next
                l2=l2.next
                l=l.next
            while l2:
                l.next=ListNode((l2.val+carryon)%10)
                carryon=(l2.val+carryon)/10
                l2=l2.next
                l=l.next
            while l1:
                l.next=ListNode((l1.val+carryon)%10)
                carryon=(l1.val+carryon)/10
                l1=l1.next
                l=l.next
            if carryon:
                l.next=ListNode(1)
            return h.next
            
## Solution:

简写：

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def addTwoNumbers(self, l1, l2):
            """
            :type l1: ListNode
            :type l2: ListNode
            :rtype: ListNode
            """
            carryon=0
            h=l=ListNode(None)
            while l1 or l2 or carryon:
                v1, v2=0, 0
                if l1:
                    v1=l1.val
                    l1=l1.next
                if l2:
                    v2=l2.val
                    l2=l2.next
                l.next=ListNode((v1+v2+carryon)%10)
                carryon=(v1+v2+carryon)/10
                l=l.next
            return h.next