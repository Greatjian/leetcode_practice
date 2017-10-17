# 337. House Robber III

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

         3
        / \
       2   3
        \   \ 
         3   1

Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:

         3
        / \
       4   5
      / \   \ 
     1   3   1

Maximum amount of money the thief can rob = 4 + 5 = 9.

## Method:

brute force recursion, tle:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def rob(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            if not root:
                return 0
            val=root.val
            if root.left:
                val+=self.rob(root.left.left)+self.rob(root.left.right)
            if root.right:
                val+=self.rob(root.right.left)+self.rob(root.right.right)
            return max(val, self.rob(root.left)+self.rob(root.right))
            
## Solution:

adding a dictionary for memorization:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def rob(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            self.d={}
            return self.helper(root)
            
        def helper(self, root):
            if not root:
                return 0
            if root in self.d:
                return self.d[root]
            val=root.val
            if root.left:
                val+=self.helper(root.left.left)+self.helper(root.left.right)
            if root.right:
                val+=self.helper(root.right.left)+self.helper(root.right.right)
            self.d[root]=max(val, self.helper(root.left)+self.helper(root.right))
            return self.d[root]
            
dp, [not chosen, chosen]:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def rob(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            return max(self.helper(root))
            
        def helper(self, root):
            if not root:
                return [0,0]
            left=self.helper(root.left)
            right=self.helper(root.right)
            res=[max(left)+max(right), left[0]+right[0]+root.val]
            return res