# 102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:

    Given binary tree [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7

return its level order traversal as:
    [
      [3],
      [9,20],
      [15,7]
    ]

## Method:

iteration:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def levelOrder(self, root):
            """
            :type root: TreeNode
            :rtype: List[List[int]]
            """
            ans, level = [], [root]
            while root and level:
                ans.append([node.val for node in level])            
                level = [leaf for node in level for leaf in (node.left, node.right) if leaf]
            return ans

using deque:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def levelOrder(self, root):
            """
            :type root: TreeNode
            :rtype: List[List[int]]
            """
            res = []
            level = collections.deque([root])
            while root and level:
                local = []
                for _ in range(len(level)):
                    t = level.popleft()
                    local.append(t.val)
                    if t.left:
                        level.append(t.left)
                    if t.right:
                        level.append(t.right)
                res.append(local)
            return res
            
recursion:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def levelOrder(self, root):
            """
            :type root: TreeNode
            :rtype: List[List[int]]
            """
            self.l=[]
            self.helper(root, 0)
            return self.l
        
        def helper(self, root, level):
            if not root:
                return
            else:
                if level==len(self.l):
                    self.l.append([])
                self.l[level].append(root.val)
                self.helper(root.left, level+1)
                self.helper(root.right, level+1)