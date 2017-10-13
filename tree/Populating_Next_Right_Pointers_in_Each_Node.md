# 116. Populating Next Right Pointers in Each Node

Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
    
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

- You may only use constant extra space.
- You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).

For example,
Given the following perfect binary tree,

         1
       /  \
      2    3
     / \  / \
    4  5  6  7

After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
    
## Method:

iterative, general solution without usingperfect binary tree condition.

O(n) space:

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

recursion:

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
            if not root:
                return
            if root.left:
                root.left.next=root.right
            if root.right and root.next:
                root.right.next=root.next.left
            self.connect(root.left)
            self.connect(root.right)
            
iteration:

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
            while root and root.left:
                cur=root
                while cur:
                    cur.left.next=cur.right
                    if cur.next:
                        cur.right.next=cur.next.left
                    cur=cur.next
                root=root.left