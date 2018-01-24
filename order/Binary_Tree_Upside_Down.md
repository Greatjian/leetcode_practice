# 156. Binary Tree Upside Down

Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.

For example:

    Given a binary tree {1,2,3,4,5},
    
        1
       / \
      2   3
     / \
    4   5
    
    return the root of the binary tree [4,5,2,#,#,3,1].
    
       4
      / \
     5   2
        / \
       3   1  
       
## Method:

Think about how you can save the tree information you need before changing the tree structure:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def upsideDownBinaryTree(self, root):
            """
            :type root: TreeNode
            :rtype: TreeNode
            """
            prev=None
            temp=None
            cur=root
            while cur:
                next=cur.left
                cur.left=temp
                temp=cur.right
                cur.right=prev
                prev=cur
                cur=next
            return prev