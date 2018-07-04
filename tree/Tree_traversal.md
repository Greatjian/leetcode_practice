# Tree traversal

## Iterative

Using stack:

- preorder(olr)
- inorder(lor)
- postorder(lro)



    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def preorderTraversal(self, root):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            res=[]
            stack=[[root, 0]] // 0: visit, 1: print
            while stack:
                root, i=stack.pop()
                if not root:
                    continue
                if i==1:
                    res.append(root.val)
                elif i==0:
                    stack.append([root.right, 0])
                    stack.append([root.left, 0])
                    stack.append([root, 1])
            return res

## Recursive

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
            
recursion, dfs(root, depth):

- [Binary Tree Level Order Traversal](/tree/Binary_Tree_Level_Order_Traversal.md)
- [Binary Tree Right Side View](/tree/Binary_Tree_Right_Side_View.md)