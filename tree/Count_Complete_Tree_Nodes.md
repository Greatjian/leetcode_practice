# 222. Count Complete Tree Nodes

Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

## Method:

do not use the condition of complete tree.

tree traversal, time limit exceeded.

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def countNodes(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            stack=[root]
            res=0
            while stack and root:
                node=stack.pop()
                res+=1
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            return res
            
recursive, tle:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def countNodes(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            if not root:
                return 0
            return self.countNodes(root.left)+self.countNodes(root.right)+1
            
## Solution:

从左侧求高度，走一次path求得：

iteration:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def countNodes(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            res=0
            while root:
                h=self.getHeight(root)
                if self.getHeight(root.right)==h-1:
                    res+=2**(h)
                    root=root.right
                else:
                    res+=2**(h-1)
                    root=root.left
            return res
        
        def getHeight(self, root):
            if not root:
                return -1
            # if not root.left and not root.right:
            #     return 0
            return 1+self.getHeight(root.left)
            
recursion:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def countNodes(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            if not root:
                return 0
            h=self.getHeight(root)
            if self.getHeight(root.right)==h-1:
                return 2**(h)+self.countNodes(root.right)
            else:
                return 2**(h-1)+self.countNodes(root.left)
        
        def getHeight(self, root):
            if not root:
                return -1
            # if not root.left and not root.right:
            #     return 0
            return 1+self.getHeight(root.left)