# 230. Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
- You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
- What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

## Method:

using inorder traversal:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def kthSmallest(self, root, k):
            """
            :type root: TreeNode
            :type k: int
            :rtype: int
            """
            stack=[]
            res=[]
            while stack or root:
                while root:
                    stack.append(root)
                    root=root.left
                root=stack.pop()
                res.append(root.val)
                root=root.right
            return res[k-1]
            
little manipulation saving space:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def kthSmallest(self, root, k):
            """
            :type root: TreeNode
            :type k: int
            :rtype: int
            """
            stack=[]
            while stack or root:
                while root:
                    stack.append(root)
                    root=root.left
                root=stack.pop()
                k-=1
                if k==0:
                    return root.val
                root=root.right