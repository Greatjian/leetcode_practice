# 114. Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6

The flattened tree should look like:

       1
        \
         2
          \
           3
            \
             4
              \
               5
                \
                 6

## Method:

recursion: 倒序遍历（右左中）插入：

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def flatten(self, root):
            """
            :type root: TreeNode
            :rtype: void Do not return anything, modify root in-place instead.
            """
            self.prev=None
            self.helper(root)
            
        def helper(self, root):
            if not root:
                return
            self.helper(root.right)
            self.helper(root.left)
            root.right=self.prev
            root.left=None
            self.prev=root