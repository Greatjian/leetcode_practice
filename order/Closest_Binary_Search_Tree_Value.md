# 270. Closest Binary Search Tree Value

Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:
- Given target value is a floating point.
- You are guaranteed to have only one unique value in the BST that is closest to the target.

## Method:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def closestValue(self, root, target):
            """
            :type root: TreeNode
            :type target: float
            :rtype: int
            """
            diff=float('inf')
            while root:
                if abs(root.val-target)<diff:
                    diff=abs(root.val-target)
                    res=root.val
                if target>root.val:
                    root=root.right
                else:
                    root=root.left
            return res
        
## Solution:

巧用min函数(lambda):

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def closestValue(self, root, target):
            """
            :type root: TreeNode
            :type target: float
            :rtype: int
            """
            res=root.val
            while root:
                res=min(root.val, res, key=lambda i: abs(i-target))
                if target>root.val:
                    root=root.right
                else:
                    root=root.left
            return res