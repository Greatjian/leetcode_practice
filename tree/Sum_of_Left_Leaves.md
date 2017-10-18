# 404. Sum of Left Leaves

Find the sum of all left leaves in a given binary tree.

Example:

        3
       / \
      9  20
        /  \
       15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

## Method:

recursion:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def sumOfLeftLeaves(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            self.res=0
            self.helper(root)
            return self.res
            
        def helper(self, root):
            if not root:
                return
            if root.left and not root.left.left and not root.left.right:
                self.res+=root.left.val
            if root.left:
                self.helper(root.left)
            if root.right:
                self.helper(root.right)
            