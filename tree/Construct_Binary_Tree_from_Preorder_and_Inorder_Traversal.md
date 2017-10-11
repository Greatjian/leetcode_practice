# 105. Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

## Method:

recursion:（299）

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def buildTree(self, preorder, inorder):
            """
            :type preorder: List[int]
            :type inorder: List[int]
            :rtype: TreeNode
            """
            if not inorder: 
                return None
            root = TreeNode(preorder[0])
            rootPos = inorder.index(preorder[0])
            root.left = self.buildTree(preorder[1 : 1 + rootPos], inorder[ : rootPos])
            root.right = self.buildTree(preorder[rootPos + 1 : ], inorder[rootPos + 1 : ])
            return root
            
 简化，减少slicing：（229）
 
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def buildTree(self, preorder, inorder):
            """
            :type preorder: List[int]
            :type inorder: List[int]
            :rtype: TreeNode
            """
            if inorder: 
                rootPos = inorder.index(preorder.pop(0))
                root = TreeNode(inorder[rootPos])
                root.left = self.buildTree(preorder, inorder[ : rootPos])
                root.right = self.buildTree(preorder, inorder[rootPos + 1 : ])
                return root
                
 recursion部分将数组用index代替：（125）
 
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def buildTree(self, preorder, inorder):
            """
            :type preorder: List[int]
            :type inorder: List[int]
            :rtype: TreeNode
            """
            
            def helper(pstart, pend, istart, iend):
                if pstart>pend or istart>iend:
                    return None
                root=TreeNode(preorder[pstart])
                rootPos = inorder.index(preorder[pstart])
                root.left = helper(pstart+1, pstart+rootPos-istart, istart ,rootPos-1)
                root.right = helper(pstart+rootPos-istart+1, pend, rootPos+1, iend)
                return root
            
            return helper(0, len(preorder)-1, 0, len(inorder)-1)
            
 
 将循环查找部分用字典代替：（52）
 
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def buildTree(self, preorder, inorder):
            """
            :type preorder: List[int]
            :type inorder: List[int]
            :rtype: TreeNode
            """
            
            def helper(pstart, pend, istart, iend):
                if pstart>pend or istart>iend:
                    return None
                root=TreeNode(preorder[pstart])
                rootPos = d[preorder[pstart]]
                root.left = helper(pstart+1, pstart+rootPos-istart, istart ,rootPos-1)
                root.right = helper(pstart+rootPos-istart+1, pend, rootPos+1, iend)
                return root
            
            d={val:idx for idx, val in enumerate(inorder)}
            return helper(0, len(preorder)-1, 0, len(inorder)-1)
            