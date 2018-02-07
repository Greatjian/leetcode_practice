# 199. Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:

Given the following binary tree,

       1            <---
     /   \
    2     3         <---
     \     \
      5     4       <---

You should return [1, 3, 4].

## Method:

bfs using queue:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def rightSideView(self, root):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            queue=collections.deque([root])
            res=[]
            while queue and root:
                level=[]
                for i in range(len(queue)):
                    node=queue.popleft()
                    level.append(node.val)
                    if node.right:
                        queue.append(node.right)
                    if node.left:
                        queue.append(node.left)
                res.append(level[0])
            return res
            
二刷：
            
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def rightSideView(self, root):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            if not root:
                return []
            res=[]
            queue=collections.deque([[root, 0]])
            depth=-1
            while queue:
                root, d=queue.popleft()
                depth=max(depth, d)
                if d==len(res):
                    res.append(root.val)
                if root.right:
                    queue.append([root.right, d+1])
                if root.left:
                    queue.append([root.left, d+1])
            return res

len, append first item each level:            
            
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def rightSideView(self, root):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            if not root:
                return []
            res=[]
            queue=collections.deque([root])
            while queue:
                flag=True
                for _ in range(len(queue)):
                    root=queue.popleft()
                    if flag:
                        res.append(root.val)
                        flag=False
                    if root.right:
                        queue.append(root.right)
                    if root.left:
                        queue.append(root.left)
            return res
            
preorder:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def rightSideView(self, root):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            res=[]
            self.helper(root, 0, res)
            return res
            
        def helper(self, root, level, res):
            if root:
                if level==len(res):
                    res.append(root.val)
                else:
                    res[level]=root.val
                self.helper(root.left, level+1, res)
                self.helper(root.right, level+1, res)

## Solution:

dfs+depth->bfs:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def rightSideView(self, root):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            self.res=[]
            self.helper(root, 0)
            return self.res
            
        def helper(self, root, depth):
            if not root:
                return
            if len(self.res)==depth:
                self.res.append(root.val)
            self.helper(root.right, depth+1)
            self.helper(root.left, depth+1)