# 226. Invert Binary Tree

Invert a binary tree.

         4
       /   \
      2     7
     / \   / \
    1   3 6   9

to

         4
       /   \
      7     2
     / \   / \
    9   6 3   1

Trivia:

This problem was inspired by this original tweet by Max Howell:

> Google: 90% of our engineers use the software you wrote (Homebrew), 
but you can’t invert a binary tree on a whiteboard so fuck off.

## Method:

recursion:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def invertTree(self, root):
            """
            :type root: TreeNode
            :rtype: TreeNode
            """
            if not root:
                return
            root.left, root.right=root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root
            
## Solution:

recursion:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def invertTree(self, root):
            """
            :type root: TreeNode
            :rtype: TreeNode
            """
            if root:
                root.left, root.right=self.invertTree(root.right), self.invertTree(root.left)            
                return root
                
iteration:

dfs using stack:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def invertTree(self, root):
            """
            :type root: TreeNode
            :rtype: TreeNode
            """
            stack=[root]
            while stack and root:
                node=stack.pop()
                node.left, node.right=node.right, node.left
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            return root
            
bfs using queue:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def invertTree(self, root):
            """
            :type root: TreeNode
            :rtype: TreeNode
            """
            queue=collections.deque([root])
            while queue and root:
                node=queue.popleft()
                node.left, node.right=node.right, node.left
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            return root