# 234. Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Follow up:
- Could you do it in O(n) time and O(1) space?

## Method:

O(n) space:

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def isPalindrome(self, head):
            """
            :type head: ListNode
            :rtype: bool
            """
            res=[]
            while head:
                res.append(head.val)
                head=head.next
            return res==res[::-1]

reverse the second half and check:

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def isPalindrome(self, head):
            """
            :type head: ListNode
            :rtype: bool
            """
            if not head or not head.next:
                return True
            fast, slow, prev=head, head, head
            while fast and fast.next:
                fast=fast.next.next
                prev=slow
                slow=slow.next
            if fast:
                slow=slow.next
                prev=prev.next
            prev.next=None
            prev=None
            while slow:
                n=slow.next
                slow.next=prev
                prev=slow
                slow=n
            while prev:
                if prev.val!=head.val:
                    return False
                prev=prev.next
                head=head.next
            return True
            
## Solution:

reverse the first half:

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def isPalindrome(self, head):
            """
            :type head: ListNode
            :rtype: bool
            """
            fast, slow, prev=head, head, None
            while fast and fast.next:
                fast=fast.next.next
                
                // prev, prev.next, slow = slow, prev, slow.next
                n=slow.next
                slow.next=prev
                prev=slow
                slow=n
                
            if fast:
                slow=slow.next
            while prev:
                if prev.val!=slow.val:
                    return False
                prev=prev.next
                slow=slow.next
            return True