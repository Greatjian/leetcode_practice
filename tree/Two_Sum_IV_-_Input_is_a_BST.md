# 653. Two Sum IV - Input is a BST

Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input: 

        5
       / \
      3   6
     / \   \
    2   4   7

    Target = 9

    Output: True
Example 2:

Input: 

        5
       / \
      3   6
     / \   \
    2   4   7

    Target = 28

    Output: False
    
## Method:

dict+recursion:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def findTarget(self, root, k):
            """
            :type root: TreeNode
            :type k: int
            :rtype: bool
            """
            self.d={}
            return self.helper(root, k)
            
        def helper(self, root, k):
            if not root:
                return False
            if k-root.val in self.d:
                return True
            self.d[root.val]=0
            return self.helper(root.left, k) or self.helper(root.right, k)
            
set+iteration:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def findTarget(self, root, k):
            """
            :type root: TreeNode
            :type k: int
            :rtype: bool
            """
            s=set()
            queue=collections.deque([root])
            while queue and root:
                node=queue.popleft()
                if k-node.val in s:
                    return True
                s.add(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            return False
            
            