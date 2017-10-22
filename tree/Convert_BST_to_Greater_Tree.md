# 538. Convert BST to Greater Tree

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:

              5
            /   \
           2     13

Output: The root of a Greater Tree like this:

             18
            /   \
          20     13
          
## Method:

reversed inorder traversal:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def convertBST(self, root):
            """
            :type root: TreeNode
            :rtype: TreeNode
            """
            self.s=0
            return self.helper(root)
            
        def helper(self, root):
            if not root:
                return
            self.helper(root.right)
            self.s+=root.val
            root.val=self.s
            self.helper(root.left)
            return root