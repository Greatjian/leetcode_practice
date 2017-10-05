# 98. Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example 1:

        2
       / \
      1   3
    Binary tree [2,1,3], return true.

Example 2:

        1
       / \
      2   3
    Binary tree [1,2,3], return false.
    
## Method:
iterative method, similar to inorder traversal:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def isValidBST(self, root):
            """
            :type root: TreeNode
            :rtype: bool
            """
            stack=[]
            pre=TreeNode(None)
            while stack or root:
                while root:
                    stack.append(root)
                    root=root.left
                root=stack.pop()
                if pre and pre.val>=root.val:
                    return False
                pre=root
                root=root.right
            return True
                
recursive method:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def isValidBST(self, root):
            """
            :type root: TreeNode
            :rtype: bool
            """
            return self.isBST(root, None, None)
                
        def isBST(self, root, minNode, maxNode):
            if not root:
                return True
            if minNode and root.val<=minNode.val or maxNode and root.val>=maxNode.val:
                return False
            return self.isBST(root.left, minNode, root) and self.isBST(root.right, root, maxNode)
          
将node变为数值亦可：

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def isValidBST(self, root):
            """
            :type root: TreeNode
            :rtype: bool
            """
            return self.isBST(root, float('-inf'), float('inf'))
                
        def isBST(self, root, min, max):
            if not root:
                return True
            if root.val<=min or root.val>=max:
                return False
            return self.isBST(root.left, min, root.val) and self.isBST(root.right, root.val, max)