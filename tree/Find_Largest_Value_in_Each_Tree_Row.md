# 515. Find Largest Value in Each Tree Row

You need to find the largest value in each row of a binary tree.

Example:

Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]

## Method:

level order traversal:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def largestValues(self, root):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            if not root:
                return []
            res=[]
            queue=collections.deque([root])
            while queue:
                level=[]
                for _ in range(len(queue)):
                    node=queue.popleft()
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                res.append(level)
            return [max(e) for e in res]
                
recursion:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def largestValues(self, root):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            res=[]
            self.helper(root, 0, res)
            return res
        
        
        def helper(self, root, level, res):
            if not root:
                return
            if level==len(res):
                res.append(root.val)
            else:
                res[level]=max(res[level], root.val)
            self.helper(root.left, level+1, res)
            self.helper(root.right, level+1, res)
                