# 450. Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

1. Search for a node to remove.
2. If the node is found, delete the node.

Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]

key = 3

        5
       / \
      3   6
     / \   \
    2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

        5
       / \
      4   6
     /     \
    2       7

Another valid answer is [5,2,6,null,4,null,7].

        5
       / \
      2   6
       \   \
        4   7
        
## Method:

recursion+分类讨论：

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def deleteNode(self, root, key):
            """
            :type root: TreeNode
            :type key: int
            :rtype: TreeNode
            """
            if not root:
                return root
            if key<root.val:
                root.left=self.deleteNode(root.left, key)
            elif key>root.val:
                root.right=self.deleteNode(root.right, key)
            else:
                if not root.left and not root.right:
                    root=None
                elif not root.left and root.right:
                    root=root.right
                elif root.left and not root.right:
                    root=root.left
                else:
                    data=self.findMin(root.right)
                    root.val=data.val
                    root.right=self.deleteNode(root.right, data.val)
            return root
                    
        def findMin(self, root):
            while root.left:
                root=root.left
            return root