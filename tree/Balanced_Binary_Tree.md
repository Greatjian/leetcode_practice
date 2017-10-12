# 110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

## Method:

recursion:

depth:

top down: O(nlogn)

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def isBalanced(self, root):
            """
            :type root: TreeNode
            :rtype: bool
            """
            if not root:
                return True
            return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.depth(root.left)-self.depth(root.right))<=1
        
        def depth(self, root):
            if not root:
                return 0
            return max(self.depth(root.left), self.depth(root.right))+1
            
height:

bottom up: O(n)

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def isBalanced(self, root):
            """
            :type root: TreeNode
            :rtype: bool
            """
            return self.dfsHeight(root) != -1
        
        def dfsHeight(self, root):
            if not root:
                return 0
            leftHeight = self.dfsHeight(root.left)
            rightHeight = self.dfsHeight(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            return max(leftHeight, rightHeight) + 1