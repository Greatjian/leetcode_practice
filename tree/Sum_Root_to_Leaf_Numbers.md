# 129. Sum Root to Leaf Numbers

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

        1
       / \
      2   3

- The root-to-leaf path 1->2 represents the number 12.
- The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.

## Method:

recursion:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def sumNumbers(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            res=[]
            self.helper(root, 0, res)
            return sum(res)
            
        def helper(self, root, path, res):
            if not root:
                return
            if not root.left and not root.right:
                res.append(path*10+root.val)
                return res
            self.helper(root.left, 10*path+root.val, res)
            self.helper(root.right, 10*path+root.val, res)
            
## Solution:

simple recursion:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def sumNumbers(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            self.res=0
            self.helper(root, 0)
            return self.res
            
        def helper(self, root, path):
            if not root:
                return
            if not root.left and not root.right:
                self.res+=path*10+root.val
                return
            self.helper(root.left, 10*path+root.val)
            self.helper(root.right, 10*path+root.val)
            
iteration:

dfs+stack:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def sumNumbers(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            if not root:
                return 0
            stack=[(root, root.val)]
            res=0
            while stack:
                node, value=stack.pop()
                if not node.left and not node.right:
                    res+=value
                if node.right:
                    stack.append((node.right, value*10+node.right.val))
                if node.left:
                    stack.append((node.left, value*10+node.left.val))
            return res
            
bfs+queue:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def sumNumbers(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            if not root:
                return 0
            queue=collections.deque([(root, root.val)])
            res=0
            while queue:
                node, value=queue.popleft()
                if not node.left and not node.right:
                    res+=value
                if node.left:
                    queue.append((node.left, value*10+node.left.val))
                if node.right:
                    queue.append((node.right, value*10+node.right.val))
            return res
            