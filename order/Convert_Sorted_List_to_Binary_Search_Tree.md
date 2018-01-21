# 109. Convert Sorted List to Binary Search Tree

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


Example:

    Given the sorted linked list: [-10,-3,0,5,9],
    
    One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
    
          0
         / \
       -3   9
       /   /
     -10  5
     
## Method:

tle:

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def sortedListToBST(self, head):
            """
            :type head: ListNode
            :rtype: TreeNode
            """
            size=0
            cur=head
            while cur:
                cur=cur.next
                size+=1
            return self.helper(head, 0, size)
            
        def helper(self, head, s, l):
            if s>=l:
                return
            cur=head
            m=(l+s)/2
            for i in range(m):
                cur=cur.next
            tree=TreeNode(cur.val)
            tree.left=self.helper(head, s, m)
            tree.right=self.helper(head, m+1, l)
            return tree
            
## Solution:

中结点，recursion:

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def sortedListToBST(self, head):
            """
            :type head: ListNode
            :rtype: TreeNode
            """
            return self.helper(head)
            
        def helper(self, head):
            if not head:
                return head
            fast=slow=head
            prev=None
            while fast and fast.next:
                fast=fast.next.next
                prev=slow
                slow=slow.next
            if prev:
                prev.next=None
            else:
                head=None
            tree=TreeNode(slow.val)
            tree.left=self.helper(head)
            tree.right=self.helper(slow.next)
            return tree