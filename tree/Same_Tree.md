# 100. Same Tree

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

## Method:
reursion:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def isSameTree(self, p, q):
            """
            :type p: TreeNode
            :type q: TreeNode
            :rtype: bool
            """
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val!=q.val:
                return False
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
                    
最后两部分可以合并为

    return p.val==q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 
       
iteration:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def isSameTree(self, p, q):
            """
            :type p: TreeNode
            :type q: TreeNode
            :rtype: bool
            """
            stack1, stack2=[p], [q]
            
            while stack1:
                node1=stack1.pop()
                node2=stack2.pop()
                if not node1 and not node2:
                    continue
                if not node1 or not node2:
                    return False
                if node1.val!=node2.val:
                    return False
    
                stack1.append(node1.left)
                stack2.append(node2.left)
                stack1.append(node1.right)
                stack2.append(node2.right)
                
            return True
            
string比较：

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def isSameTree(self, p, q):
            """
            :type p: TreeNode
            :type q: TreeNode
            :rtype: bool
            """
            return self.preorderPrint(p)==self.preorderPrint(q)
            
        def preorderPrint(self, root):
            if not root:
                return 'a'
            return str(root.val)+self.preorderPrint(root.left)+self.preorderPrint(root.right)