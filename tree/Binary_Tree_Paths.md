# 257. Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

       1
     /   \
    2     3
     \
      5
      
All root-to-leaf paths are:

    ["1->2->5", "1->3"]
    
## Method:

recursion:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def binaryTreePaths(self, root):
            """
            :type root: TreeNode
            :rtype: List[str]
            """
            res=[]
            self.helper(root, '', res)
            return res
            
            
        def helper(self, root, path, res):
            if not root:
                return
            if not root.left and not root.right:
                res.append(path+str(root.val))
                return
            self.helper(root.left, path+str(root.val)+'->', res)
            self.helper(root.right, path+str(root.val)+'->', res)
            
iteration

dfs using stack:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def binaryTreePaths(self, root):
            """
            :type root: TreeNode
            :rtype: List[str]
            """
            if not root:
                return []
            res=[]
            stack=[[root, str(root.val)]]
            while stack:
                node, path=stack.pop()
                if not node.left and not node.right:
                    res.append(path)
                if node.right:
                    stack.append([node.right, path+'->'+str(node.right.val)])
                if node.left:
                    stack.append([node.left, path+'->'+str(node.left.val)])
            return res
                    
bfs using queue:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def binaryTreePaths(self, root):
            """
            :type root: TreeNode
            :rtype: List[str]
            """
            if not root:
                return []
            res=[]
            queue=collections.deque([[root, str(root.val)]])
            while queue:
                node, path=queue.popleft()
                if not node.left and not node.right:
                    res.append(path)
                if node.right:
                    queue.append([node.right, path+'->'+str(node.right.val)])
                if node.left:
                    queue.append([node.left, path+'->'+str(node.left.val)])
            return res
                    