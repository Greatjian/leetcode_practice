# 783. Minimum Distance Between BST Nodes

Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

    Example :
    
    Input: root = [4,2,6,1,3,null,null]
    Output: 1
    Explanation:
    Note that root is a TreeNode object, not an array.
    
    The given tree [4,2,6,1,3,null,null] is represented by the following diagram:
    
              4
            /   \
          2      6
         / \    
        1   3  

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.

Note:

- The size of the BST will be between 2 and 100.
- The BST is always valid, each node's value is an integer, and each node's value is different.

## Method:

recursion:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def minDiffInBST(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            if not root:
                return float('inf')
            left=self.minDiffInBST(root.left)
            right=self.minDiffInBST(root.right)
            m=min(left, right)
            if root.left:
                l=root.left
                while l.right:
                    l=l.right
                m=min(m, abs(root.val-l.val))
            if root.right:
                r=root.right
                while r.left:
                    r=r.left
                m=min(m, abs(root.val-r.val))
            return m
            
## Solution:

inorder traversal, O(1) space need prev:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def minDiffInBST(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            self.prev=float('-inf')
            self.m=float('inf')
            self.inorder(root)
            return self.m
            
        def inorder(self, root):
            if not root:
                return
            self.inorder(root.left)
            self.m=min(self.m, root.val-self.prev)
            self.prev=root.val
            self.inorder(root.right)
            