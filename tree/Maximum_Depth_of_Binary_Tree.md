# 104. Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## Method:

recursion:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def maxDepth(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            self.l=0
            self.helper(root, 1)
            return self.l
            
        def helper(self, root, m):
            if not root:
                return
            self.l=max(self.l, m)
            self.helper(root.left, m+1)
            self.helper(root.right, m+1)
            
## Solution:

简洁recursion:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def maxDepth(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            if not root:
                return 0
            return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
            
iteration:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def maxDepth(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            depth=0
            level=[root]
            while level and root:
                nlevel=[]
                for node in level:
                    if node.left:
                        nlevel.append(node.left)
                    if node.right:
                        nlevel.append(node.right)
                depth+=1
                level=nlevel
            return depth