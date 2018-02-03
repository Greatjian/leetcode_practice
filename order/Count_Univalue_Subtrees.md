# 250. Count Univalue Subtrees

Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

    For example:
    Given binary tree,
                  5
                 / \
                1   5
               / \   \
              5   5   5
              
    return 4.

## Method:

tle:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def countUnivalSubtrees(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            return self.helper(root)[0]
            
        def helper(self, root):
            if not root:
                return (0, None)
            if not root.left and not root.right:
                return (1, root.val)
            left=self.helper(root.left)[0]
            right=self.helper(root.right)[0]
            if self.helper(root.left)[1] in [None, root.val] and self.helper(root.right)[1] in[None, root.val]:
                res=(right+left+1, root.val)
            else:
                res=(right+left, float('inf'))
            return res
            
逐根提前判断(None, root.val, float('inf')三种情况)，返回两个数值：

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def countUnivalSubtrees(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            return self.helper(root)[0]
            
        def helper(self, root):
            if not root:
                return (0, None)
            if not root.left and not root.right:
                return (1, root.val)
            left=self.helper(root.left)
            right=self.helper(root.right)
            if left[1]==float('inf') or right[1]==float('inf'):
                return (right[0]+left[0], float('inf'))
            if left[1] in [None, root.val] and right[1] in [None, root.val]:
                res=(right[0]+left[0]+1, root.val)
            else:
                res=(right[0]+left[0], float('inf'))
            return res
            
## Solution:

helper boolean function + count:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def countUnivalSubtrees(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            self.cnt=0
            self.valid(root)
            return self.cnt
            
        def valid(self, root):
            if not root:
                return False
            if not root.left and not root.right:
                self.cnt+=1
                return True
            left=True if not root.left or (self.valid(root.left) and root.val==root.left.val) else False
            right=True if not root.right or (self.valid(root.right) and root.val==root.right.val) else False
            if left and right:
                self.cnt+=1
                return True
            return False