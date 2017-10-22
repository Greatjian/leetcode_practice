# 513. Find Bottom Left Tree Value

Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:

Input:

        2
       / \
      1   3

Output:

    1

Example 2: 

Input:

            1
           / \
          2   3
         /   / \
        4   5   6
           /
          7

Output:

    7

Note: You may assume the tree (i.e., the given root node) is not NULL.

## Method:

level order traversal:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def findBottomLeftValue(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            res=[]
            queue=collections.deque([root])
            while queue:
                level=[]
                for _ in range(len(queue)):
                    node=queue.popleft()
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                res.append(level)
            return res[-1][0]
            
recursion:

保存value, height:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def findBottomLeftValue(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            return self.helper(root)[0]
            
        def helper(self, root):
            if not root:
                return 0, -1
            if not root.left and not root.right:
                return root.val, 0
            lv, lh=self.helper(root.left)
            rv, rh=self.helper(root.right)
            if lh>=rh:
                return lv, lh+1
            return rv, rh+1
            