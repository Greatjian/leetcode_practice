# 145. Binary Tree Postorder Traversal


Given a binary tree, return the postorder traversal of its nodes' values.

    For example:
    Given binary tree {1,#,2,3},
       1
        \
         2
        /
       3
    return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?

## Method:

recursion:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def postorderTraversal(self, root):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            self.res=[]
            self.helper(root)
            return self.res
        
        def helper(self, root):
            if not root:
                return
            self.helper(root.left)
            self.helper(root.right)
            self.res.append(root.val)
            
iteration:

preorder【中左右】改为【中右左】后倒序插入：

    class Solution(object):
        def postorderTraversal(self, root):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            ans=[]
            stack=[root]
            while stack and root:
                node=stack.pop()
                if node:
                    ans.append(node.val)
                    stack.append(node.left)
                    stack.append(node.right)
            return ans[::-1]
            