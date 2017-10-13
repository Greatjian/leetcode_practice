# 117. Populating Next Right Pointers in Each Node II

Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.

For example,
Given the following binary tree,

         1
       /  \
      2    3
     / \    \
    4   5    7

After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
    
## Method:

O(n) space, general solution same as the previous one:

    # Definition for binary tree with next pointer.
    # class TreeLinkNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    #         self.next = None
    
    class Solution:
        # @param root, a tree link node
        # @return nothing
        def connect(self, root):
            queue=collections.deque([root])
            while queue and root:
                nqueue=collections.deque([])
                prev=None
                while queue:
                    node=queue.pop()
                    node.next=prev
                    prev=node
                    if node.right:
                        nqueue.appendleft(node.right)
                    if node.left:
                        nqueue.appendleft(node.left)
                queue=nqueue
                
## Solution:

iterative:

    # Definition for binary tree with next pointer.
    # class TreeLinkNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    #         self.next = None
    
    class Solution:
        # @param root, a tree link node
        # @return nothing
        def connect(self, root):
            while root:
                cur=TreeLinkNode(0)
                nroot=cur
                while root:
                    if root.left:
                        cur.next=root.left
                        cur=cur.next
                    if root.right:
                        cur.next=root.right
                        cur=cur.next
                    root=root.next
                root=nroot.next