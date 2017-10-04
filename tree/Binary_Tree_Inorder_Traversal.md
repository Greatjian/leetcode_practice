# 94. Binary Tree Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes' values.

For example:

    Given binary tree [1,null,2,3],
       1
        \
         2
        /
       3
    return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?

## Method:

recursive method:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def inorderTraversal(self, root):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            def helper(root):
                if root:
                    helper(root.left)
                    self.l.append(root.val)
                    helper(root.right)
                        
            self.l=[]
            helper(root)
            return self.l
            
iterative method:
    
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def inorderTraversal(self, root):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            ans=[]
            stack=[]
            while stack or root:
                while root:
                    stack.append(root)
                    root=root.left
                root=stack.pop()
                ans.append(root.val)
                root=root.right
            return ans