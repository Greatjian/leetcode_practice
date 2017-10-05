# 101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

        1
       / \
      2   2
     / \ / \
    3  4 4  3

But the following [1,2,2,null,3,null,3] is not:

        1
       / \
      2   2
       \   \
       3    3
   
Note:
- Bonus points if you could solve it both recursively and iteratively.

## Method:

recursion:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def isSymmetric(self, root):
            """
            :type root: TreeNode
            :rtype: bool
            """
            return self.helper(root, root)
            
        def helper(self, left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val==right.val and self.helper(left.right, right.left) and self.helper(left.left, right.right)
            
iteration:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def isSymmetric(self, root):
            """
            :type root: TreeNode
            :rtype: bool
            """
            stack1, stack2=[root], [root]
            
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
                stack2.append(node2.right)
                stack1.append(node1.right)
                stack2.append(node2.left)
                
            return True