# 543. Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:

Given a binary tree 

          1
         / \
        2   3
       / \     
      4   5    

Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

## Method:

over-recursion:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def diameterOfBinaryTree(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            if not root:
                return 0
            return max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right), self.helper(root.left)+self.helper(root.right))
        
        def helper(self, root):
            if not root:
                return 0
            return max(self.helper(root.left), self.helper(root.right))+1
            
## Solution:

depth recursion+count:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def diameterOfBinaryTree(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            self.m=0
            self.helper(root)
            return self.m
        
        def helper(self, root):
            if not root:
                return 0
            left=self.helper(root.left)
            right=self.helper(root.right)
            self.m=max(self.m, left+right)
            return max(left,right)+1
        
                      