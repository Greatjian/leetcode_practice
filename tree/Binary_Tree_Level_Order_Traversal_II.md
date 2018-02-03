# 107. Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:

Given binary tree [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7

return its bottom-up level order traversal as:
    
    [
      [15,7],
      [9,20],
      [3]
    ]
    
## Method:
参考102，最后反向：

list:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def levelOrderBottom(self, root):
            """
            :type root: TreeNode
            :rtype: List[List[int]]
            """
            res=[]
            level=[root]
            while level and root:
                nlevel=[]
                res.append([node.val for node in level])
                for node in level:
                    if node.left:
                        nlevel.append(node.left)
                    if node.right:
                        nlevel.append(node.right)
                level=nlevel
            return res[::-1]

deque:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def levelOrderBottom(self, root):
            """
            :type root: TreeNode
            :rtype: List[List[int]]
            """
            res=[]
            queue=collections.deque([root])
            while root and queue:
                level=[]
                for _ in range(len(queue)):
                    node=queue.popleft()
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                res.append(level)
            return res[::-1]  