# 106. Construct Binary Tree from Inorder and Postorder Traversal

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

## Method:

仿照前题：

recursion slicing: (305)

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def buildTree(self, inorder, postorder):
            """
            :type inorder: List[int]
            :type postorder: List[int]
            :rtype: TreeNode
            """
            if not postorder:
                return
            root=TreeNode(postorder[-1])
            rootPos=inorder.index(root.val)
            root.left=self.buildTree(inorder[:rootPos], postorder[:rootPos])
            root.right=self.buildTree(inorder[rootPos+1:], postorder[rootPos:-1])
            return root
            
using index: (152)

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def buildTree(self, inorder, postorder):
            """
            :type inorder: List[int]
            :type postorder: List[int]
            :rtype: TreeNode
            """    
            def helper(i1, i2, p1, p2):
                if i1>i2 or p1>p2:
                    return
                root=TreeNode(postorder[p2])
                rootPos=inorder.index(root.val)
                root.left=helper(i1, rootPos-1, p1, p1+rootPos-1-i1)
                root.right=helper(rootPos+1, i2, p1+rootPos-i1, p2-1)
                return root
                
            return helper(0, len(inorder)-1, 0, len(postorder)-1)
            
using dictionary: (55)

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def buildTree(self, inorder, postorder):
            """
            :type inorder: List[int]
            :type postorder: List[int]
            :rtype: TreeNode
            """    
            def helper(i1, i2, p1, p2):
                if i1>i2 or p1>p2:
                    return
                root=TreeNode(postorder[p2])
                rootPos=self.d[root.val]
                root.left=helper(i1, rootPos-1, p1, p1+rootPos-1-i1)
                root.right=helper(rootPos+1, i2, p1+rootPos-i1, p2-1)
                return root
            
            self.d={val:idx for idx,val in enumerate(inorder)}    
            return helper(0, len(inorder)-1, 0, len(postorder)-1)