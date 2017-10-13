# Tree traversal

## Preorder

iteration, using stack:

    class Solution(object):
        def preorderTraversal(self, root):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            res=[]
            stack=[root]
            while stack and root:
                node=stack.pop()
                res.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            return res
            
recursion:

    class Solution(object):
        def preorderTraversal(self, root):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            self.l=[]
            self.helper(root)
            return self.l
            
        def helper(self, root):
            if not root:
                return
            self.l.append(root.val)
            self.helper(root.left)
            self.helper(root.right)
            
## Inorder

iteration, using stack:

    class Solution(object):
        def inorderTraversal(self, root):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            ans=[]
            stack=[]
            while stack or root:
                while root:
                    stack.append(root)
                    root=root.left
                root=stack.pop()
                ans.append(root.val)
                root=root.right
            return ans
            
recursion:

    class Solution(object):
        def inorderTraversal(self, root):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            def helper(root):
                if root:
                    helper(root.left)
                    self.l.append(root.val)
                    helper(root.right)
                        
            self.l=[]
            helper(root)
            return self.l
            
## Postorder:

iteration:

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
            
recursion:

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
            
## Level order

iteration, using queue:

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
            queue = collections.deque([root])
            while root and level:
                level = []
                for _ in range(len(queue)):
                    node = queue.popleft()
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                res.append(level)
            return res