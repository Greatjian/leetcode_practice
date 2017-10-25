# 687. Longest Univalue Path

Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

    2

Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

    2

Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.

## Method:

similar to previous problem [Diameter of binary tree](/tree/Diameter_of_Binary_Tree.md).

recursion:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def longestUnivaluePath(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            self.c=0
            self.helper(root)
            return self.c
            
        def helper(self, root):
            if not root:
                return 0
            left=self.helper(root.left)
            right=self.helper(root.right)
            leftlen=left+1 if root.left and root.left.val==root.val else 0
            rightlen=right+1 if root.right and root.right.val==root.val else 0
            self.c=max(self.c, leftlen+rightlen)
            return max(leftlen, rightlen)